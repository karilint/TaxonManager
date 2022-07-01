from django.db import models  # pylint:disable=W0611

from django.db import models
import json
import urllib.request
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.error import HTTPError
from .utils import ensure_https, add_optional_kv
from django.utils import timezone
from django_userforeignkey.models.fields import UserForeignKey
from simple_history.models import HistoricalRecords

# (null=True, blank=True) allows empty fields, makes testing easier for now

class BaseModel(models.Model):
    created_by = UserForeignKey(auto_user_add=True, related_name='%(class)s_createdby')
    modified_by = UserForeignKey(auto_user=True, related_name='%(class)s_modifiedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)
    
    class Meta:
        abstract = True

class Reference(BaseModel):
    """A literature reference, for example a journal article, book etc."""

    source_type = 'article'

    id = models.AutoField(primary_key=True)

    # A list of the authors' names in a string as:
    # 'A. N. Other, B.-C. Person Jr., Ch. Someone-Someone, N. M. L. Haw Haw'
    # DO NOT separate names with "AND" (even before the last author).
    authors = models.TextField(blank=True,
        help_text='Comma-delimited names with space-separated initials first'
                  ' (no ANDs). e.g. "A. N. Other, B.-C. Person Jr., Ch. '
                  'Someone-Someone, N. M. L. Haw Haw"')

    # The article, book, or thesis title.
    title = models.TextField(blank=True,
        help_text='Best-effort UTF-8 encoded plaintext version of title. No'
                  ' HTML tags, markdown or LaTeX.')
    # The title as HTML.
    title_html = models.TextField(blank=True,
        help_text="Valid HTML version of title. Don't wrap with &lt;p&gt; or"
                  " other tags.")
    # The title as LaTeX.
    title_latex = models.TextField(blank=True,
        help_text="LaTeX version of title. Don't escape backslashes (\\) but"
                  " do use valid LaTeX for accented and similar characers.")

    # The journal name.
    journal = models.CharField(max_length=500, blank=True)
    # The volume (which may be a string).
    volume = models.CharField(max_length=10, blank=True)
    # The first page (which may be a string e.g. 'L123').
    page_start = models.CharField(max_length=10, blank=True)
    # The last page
    page_end = models.CharField(max_length=10, blank=True)
    # Article number, used instead of page number by some journals (e.g.
    # J. Chem. Phys.)
    article_number = models.CharField(max_length=16, blank=True)

    # The publication year (as an integer, YYYY).
    year = models.IntegerField(null=True, blank=True)

    # For flexibility, allow free-form "notes" as references, e.g.
    # private communications, comments, etc.
    note = models.TextField(blank=True)
    # the note as HTML
    note_html = models.TextField(blank=True)
    # the note as LaTeX
    note_latex = models.TextField(blank=True)

    # the Digital Object Identifier, if available.
    doi = models.CharField(max_length=100, blank=True)
    # the Nasa/ADS Bibcode, if available.
    bibcode = models.CharField(max_length=19, blank=True)
    # a URL to the source, if available; if not provided the model will
    # construct https://dx.doi.org/<DOI>
    url = models.URLField(blank=True,
        help_text="If not provided, this will be automatically constructed"
                  " as https://dx.doi.org/&lt;DOI&gt; if possible.")

    # BibTeX entry as a string.
    bibtex = models.TextField(null=True, blank=True)
    # Research Information Systems (RIS) standardized tag formatted string.
    ris = models.TextField(null=True, blank=True)
    # JSON text string in CiteProc format.
    citeproc_json = models.TextField(null=True, blank=True)

    visible = models.IntegerField(default=1)

    class Meta:
        app_label = 'front'


    def _get_or_missing(self, field_name):
        """Try to get the value of field_name or say it's missing."""

        s = getattr(self, field_name)
        if not s:
            return '[missing {}]'.format(field_name)
        return s

    def __str__(self):
        """Simple string representation of the reference."""

        return '{}: {}, {}'.format(self.id, self._get_or_missing('authors'),
                                   self._get_or_missing('title'))

    @property
    def qualified_id(self):
        """Return the Ref's Primary Key ID as a string, prefixed with 'B'."""
        return 'B{}'.format(self.id)

    def _make_url_html(self, s_url=None):
        """Try to make an HTML <a> tag for the reference's URL."""

        if s_url is None:
            s_url = self.url
        if s_url:
            url_or_doi = self.doi or s_url
            return '<span class="noprint"> [<a href="{}">{}'\
                    '</a>]</span>'.format(s_url, url_or_doi)
        return ''

    def _make_url_html_from_doi(self):
        """Try to make an HTML <a> tag from the reference's DOI."""

        if self.doi:
            s_url = 'https://dx.doi.org/{}'.format(self.doi)
            return self._make_url_html(s_url)
        return ''

    @property
    def authors_list(self):
        return [e.strip() for e in self.authors.split(',')]

    def shorten_authors(self, nmax=5, nret=1):
        """
        Return a shortened list of authors, limited to nret names plus "et al."
        if there are more than nmax authors associated with a Ref object.
        If nmax is None, then return all author names.
        """

        if nmax == None:
            return self.authors

        if not self.authors:
            return ''
        authors = self.authors.split(',')
        nauthors = len(authors)

        if nauthors == 1:
            return self.authors

        if nauthors > nmax:
            return ', '.join(authors[:nret]) + ' et al.'

        return ', '.join(authors[:nauthors-1]) + ' and ' + authors[-1]

    def parse_authors(self):
        """Parse the authors string to a list of (initials, surname) tuples."""

        s_authors = self.authors.split(',')
        l_authors = []
        for author in s_authors:
            initials = []
            fragments = author.split()
            for i, s in enumerate(fragments):
                if s[-1] == '.':
                    initials.append(s.strip())
                else:
                   break
            surname = ' '.join(fragments[i:])
            l_authors.append( (initials, surname) )
        return l_authors

    def _get_html_title(self):
        """Return the HTML title, if possible; otherwise use plain text."""

        return self.title_html or self._get_or_missing('title')

    def html_article(self, pk=True, authors_nmax=None):
        """Return the HTML markup for the Ref."""

        s_pk = ''
        if pk:
            s_pk = 'B{}: '.format(self.pk)
        s_authors = self.shorten_authors(nmax=authors_nmax)
        if s_authors:
            s_authors += ', '
        s_title = '"{}"'.format(self._get_html_title())
        s_journal = '<em>{}</em>'.format(self._get_or_missing('journal'))
        s_volume = ' <b>{}</b>'.format(self.volume) if self.volume else ''
        s_pages = ' '
        if self.page_start:
            if self.page_end:
                s_pages = ', {}-{}'.format(self.page_start, self.page_end)
            else:
                s_pages = ', {}'.format(self.page_start)

        s_article_number = ' '
        if self.article_number:
            s_article_number = ', {} '.format(self.article_number)
            s_pages = ''
        elif s_pages != ' ':
            s_article_number = ''

        s_year = '({})'.format(self.year) if self.year else ''
        s_url = self._make_url_html() or self._make_url_html_from_doi()

        s = '{s_pk}{authors}{title}, {journal}{volume}{pages}'\
            '{article_number} {year}. {url}'.format(s_pk=s_pk,
            authors=s_authors, title=s_title, journal=s_journal,
            volume=s_volume, pages=s_pages, article_number=s_article_number,
            year=s_year, url=s_url)
        return s

    def html(self, *args, **kwargs):
        """Return the HTML markup for the Ref."""

        return self.html_article(*args, **kwargs)

    def json(self):
        """Export the Ref as JSON."""

        return json.dumps(self.serialize())

    def serialize(self):
        d = {'qid': self.qualified_id,
             'source-type': self.source_type}
        if self.authors:
            d['authors'] = self.authors_list
        fields = ('title', 'journal', 'volume', 'page-start', 'page-end',
                  'article-number', 'year', 'note', 'doi', 'bibcode', 'url')
        for k in fields:
            add_optional_kv(d, k, self)
        return d


class Comment(BaseModel):
    commentator = models.CharField(max_length=100)
    comment_detail = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.commentator}"


class Kingdom(BaseModel):
    kingdom_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.kingdom_name}"


class TaxonUnitType(BaseModel):
    class Meta:
        unique_together = (('kingdom', 'rank_id'))

    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(null=True, blank=True)
    rank_name = models.CharField(max_length=15)
    dir_parent_rank_id = models.IntegerField(null=True, blank=True)
    req_parent_rank_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Kingdom: {self.kingdom}, rank_name: {self.rank_name}, rank_id:{self.rank_id}"

class GeographicDiv(BaseModel):
    """ Model of a geographical division """

    geographic_value = models.CharField(max_length=45, null=True, blank=True)

    # Relationship defining experts for a given geographical area
    # experts = models.ManyToManyField(
    #     'Expert', through='ExpertsGeographicDiv'
    # )

    def __str__(self):
        return f"{self.geographic_value}"

class TaxonAuthorLkp(BaseModel):
    class Meta:
        unique_together = (('taxon_author_id', 'kingdom_id'))

    taxon_author_id = models.AutoField(primary_key=True)
    taxon_author = models.CharField(max_length=100, null=True, blank=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    short_author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.taxon_author}"

class Expert(BaseModel):
    """ Database model of Experts table """
    # TODO: expert_id_prefix left out, this is a char field
    # that only contains EXP presumably for all rows.
    expert = models.CharField(max_length=100)
    exp_comment = models.CharField(max_length=500, null=True, blank=True)
    geographic_div = models.ManyToManyField(GeographicDiv)

    def __str__(self):
        return f"{self.expert}"

class TaxonomicUnit(BaseModel):
    """
    Taxonomic Units
    """
    taxon_id = models.AutoField(primary_key=True)
    unit_ind1 = models.CharField(max_length=1, null=True, blank=True)
    unit_name1 = models.CharField(max_length=35)
    unit_ind2 = models.CharField(max_length=1, null=True, blank=True)
    unit_name2 = models.CharField(max_length=35, null=True, blank=True)
    unit_ind3 = models.CharField(max_length=7, null=True, blank=True)
    unit_name3 = models.CharField(max_length=35, null=True, blank=True)
    unit_ind4 = models.CharField(max_length=7, null=True, blank=True)
    unit_name4 = models.CharField(max_length=35, null=True, blank=True)
    unnamed_taxon_ind = models.CharField(max_length=1, null=True, blank=True)
    name_usage = models.CharField(max_length=12, null=True, blank=True)
    unaccept_reason = models.CharField(max_length=50, null=True, blank=True)
    credibility_rtng = models.CharField(max_length=40, null=True, blank=True)
    completeness_rtng = models.CharField(max_length=10, null=True, blank=True)
    currency_rating = models.CharField(max_length=7, null=True, blank=True)
    phylo_sort_seq = models.IntegerField(null=True, blank=True)
    parent_id = models.IntegerField()
    taxon_author = models.ForeignKey(
        TaxonAuthorLkp, on_delete=models.CASCADE, null=True, blank=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank = models.ForeignKey(TaxonUnitType, on_delete=models.CASCADE, null=True)
    hybrid_author_id = models.IntegerField(null=True, blank=True)
    uncertain_prnt_ind = models.CharField(max_length=3, null=True, blank=True)
    n_usage = models.CharField(max_length=12, null=True, blank=True)
    complete_name = models.CharField(max_length=300, null=True, blank=True)
    references = models.ManyToManyField(Reference)
    geographic_div = models.ManyToManyField(GeographicDiv)
    expert = models.ManyToManyField(Expert, null=True, blank=True)

    # Relationships
    comments = models.ManyToManyField(
        'Comment', through='TuCommentLink'
    )

    def __str__(self):
        return f"{self.unit_name1}, Kingdom: {self.kingdom} (taxon_id: {self.taxon_id}, parent_id: {self.parent_id})"

class Hierarchy(BaseModel):
    """
    Describes hierarchies, I guess?
    """
    hierarchy_string = models.CharField(max_length=128, null=True, blank=True)
    # models.IntegerField(null=True)#
    taxon = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)
    parent_id = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    childrencount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"hierarchy_string: {self.hierarchy_string}"


class TuCommentLink(BaseModel):
    """
    Many-to-many table between Comment and TaxonomicUnit tables
    """
    taxon = models.ForeignKey(
        TaxonomicUnit, on_delete=models.CASCADE)  # models.IntegerField(null=True)#
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"taxon_id: {self.taxon}, comment_id: {self.comment}"


class Publication(BaseModel):
    class Meta:
        unique_together = (('pub_id_prefix', 'publication_id'))

    pub_id_prefix = models.CharField(max_length=3, unique=True)
    publication_id = models.IntegerField(primary_key=True)
    reference_author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255)
    publication_name = models.CharField(max_length=255, null=True, blank=True)
    listed_pub_date = models.DateTimeField(null=True, blank=True)
    actual_pub_date = models.DateTimeField(null=True, blank=True)
    publisher = models.CharField(max_length=80, null=True, blank=True)
    pub_place = models.CharField(max_length=40, null=True, blank=True)
    isbn = models.CharField(max_length=16, null=True, blank=True)
    issn = models.CharField(max_length=40, null=True, blank=True)
    pages = models.CharField(max_length=15, null=True, blank=True)
    pub_comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Title: {self.title} Author: {self.reference_author}, Publication name: {self.publication_name}"


class ReferenceLink(BaseModel):
    class Meta:
        unique_together = (('taxon', 'doc_id_prefix', 'documentation'))

    # doc_id_prefix identifies the reference as a
    # publication, expert or other source
    DOC_ID_PREFIX_CHOICES = [
        ('EXP', 'Expert'),
        ('PUB', 'Publication'),
        ('SRC', 'Other source')
    ]

    taxon = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)
    doc_id_prefix = models.CharField(
        max_length=3,
        choices=DOC_ID_PREFIX_CHOICES
    )
    documentation = models.ForeignKey(
        Publication, to_field='publication_id', on_delete=models.CASCADE)
    # TODO: made des desc for clarity. Change database schema to match!
    original_desc_ind = models.CharField(max_length=1)
    init_itis_desc_ind = models.CharField(max_length=1)
    change_track_id = models.IntegerField()
    vernacular_name = models.CharField(max_length=80)

    def __str__(self):
        return f"taxon_id: {self.taxon}, documentation_id = {self.documentation}"


class ExpertsGeographicDiv(BaseModel):
    """ join-table between Expert and
    GeographicDiv tables """
    # FIXME: Connecting the ExpertsGeographicDiv with TSN might not work
    # correctly to achieve many-to-many relationship between experts and
    # geographic areas. If we defined an ID to GeographicDiv table, this
    # may work better. This is just a hunch though.
    geographic = models.ForeignKey(
        GeographicDiv, on_delete=models.CASCADE, default=1)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)

    def __str__(self):
        return f"geographic_id: {self.geographic}, expert: {self.expert}"


class SynonymLink(BaseModel):
    # FIXME: Couldn't get this to work with two FKs with both pointing to
    # tsn column in TaxonomicUnit table
    synonym_id = models.IntegerField()
    taxon_id_accepted = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)

    def __str__(self):
        return "synonym_id: {}, taxon_id_accepted: {}".format(
            self.synonym_id,
            self.taxon_id_accepted,
        )

