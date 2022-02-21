from django.db import models  # pylint:disable=W0611

from email.policy import default
from django.db import models
import json
import urllib.request
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.error import HTTPError
from .utils import ensure_https, add_optional_kv

# (null=True, blank=True) allows empty fields, makes testing easier for now


class Comment(models.Model):
    commentator = models.CharField(max_length=100)
    comment_detail = models.TextField(max_length=2000)
    comment_time_stamp = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.commentator} ({self.comment_time_stamp})"

# Create your models here.


class Kingdom(models.Model):
    kingdom_name = models.CharField(max_length=20)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.kingdom_name}"


class TaxonUnitType(models.Model):
    class Meta:
        unique_together = (('kingdom', 'rank_id'))

    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(null=True, blank=True)
    rank_name = models.CharField(max_length=15)
    dir_parent_rank_id = models.IntegerField(null=True, blank=True)
    req_parent_rank_id = models.IntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Kingdom: {self.kingdom}, rank_name: {self.rank_name}, rank_id:{self.rank_id}"


class TaxonAuthorLkp(models.Model):
    class Meta:
        unique_together = (('taxon_author_id', 'kingdom_id'))

    taxon_author_id = models.IntegerField(primary_key=True)
    taxon_author = models.CharField(max_length=100, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    short_author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.taxon_author}"


class TaxonomicUnit(models.Model):
    """
    Taxonomic Units
    """
    tsn = models.AutoField(primary_key=True)
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
    initial_time_stamp = models.DateTimeField(null=True, blank=True)
    parent_tsn = models.IntegerField()
    taxon_author_id = models.ForeignKey(
        TaxonAuthorLkp, on_delete=models.CASCADE)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(null=True, blank=True)
    hybrid_author_id = models.IntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    uncertain_prnt_ind = models.CharField(max_length=3, null=True, blank=True)
    n_usage = models.CharField(max_length=12, null=True, blank=True)
    complete_name = models.CharField(max_length=300, null=True, blank=True)

    # Relationships
    comments = models.ManyToManyField(
        'Comment', through='TuCommentLink'
    )

    def __str__(self):
        return f"{self.unit_name1}, Kingdom: {self.kingdom} (tsn_id: {self.tsn}, parent_tsn: {self.parent_tsn})"


class Hierarchy(models.Model):
    """
    Describes hierarchies, I guess?
    """
    hierarchy_string = models.CharField(max_length=128, null=True, blank=True)
    # models.IntegerField(null=True)#
    tsn = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)
    parent_tsn = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    childrencount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"hiearchy_string: {self.hierarchy_string})"


class TuCommentLink(models.Model):
    """
    Many-to-many table between Comment and TaxonomicUnit tables
    """
    tsn = models.ForeignKey(
        TaxonomicUnit, on_delete=models.CASCADE)  # models.IntegerField(null=True)#
    comment_id = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"tsn: {self.tsn}, comment_id: {self.comment_id}"


class Publication(models.Model):
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
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Title: {self.title} Author: {self.reference_author}, Publication name: {self.publication_name}"


class ReferenceLink(models.Model):
    class Meta:
        unique_together = (('tsn', 'doc_id_prefix', 'documentation_id'))

    # doc_id_prefix identifies the reference as a
    # publication, expert or other source
    DOC_ID_PREFIX_CHOICES = [
        ('EXP', 'Expert'),
        ('PUB', 'Publication'),
        ('SRC', 'Other source')
    ]

    tsn = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)
    doc_id_prefix = models.CharField(
        max_length=3,
        choices=DOC_ID_PREFIX_CHOICES
    )
    documentation_id = models.ForeignKey(
        Publication, to_field='publication_id', on_delete=models.CASCADE)
    # TODO: made des desc for clarity. Change database schema to match!
    original_desc_ind = models.CharField(max_length=1)
    init_itis_desc_ind = models.CharField(max_length=1)
    change_track_id = models.IntegerField()
    vernacular_name = models.CharField(max_length=80)
    update_date = models.DateTimeField()

    def __str__(self):
        return f"tsn: {self.tsn}, documentation_id = {self.documentation_id}"


class Expert(models.Model):
    """ Database model of Experts table """
    # TODO: expert_id_prefix left out, this is a char field
    # that only contains EXP presumably for all rows.
    expert = models.CharField(max_length=100)
    exp_comment = models.CharField(max_length=500)
    update_date = models.DateTimeField()

    def __str__(self):
        return f"Expert name: {self.expert}"


class GeographicDiv(models.Model):
    """ Model of a geographical division """

    class Meta:
        unique_together = (('tsn', 'geographic_value'))

    # TODO: This causes a warning, but this is left as is
    # until we understand the requirements better.
    tsn = models.ForeignKey(
        TaxonomicUnit,
        on_delete=models.CASCADE,
        unique=True
    )
    geographic_value = models.CharField(max_length=45, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

    # Relationship defining experts for a given geographical area
    experts = models.ManyToManyField(
        'Expert', through='ExpertsGeographicDiv'
    )

    def __str__(self):
        return f"{self.geographic_value}"


class ExpertsGeographicDiv(models.Model):
    """ join-table between Expert and
    GeographicDiv tables """
    # FIXME: Connecting the ExpertsGeographicDiv with TSN might not work
    # correctly to achieve many-to-many relationship between experts and
    # geographic areas. If we defined an ID to GeographicDiv table, this
    # may work better. This is just a hunch though.
    geographic_tsn = models.ForeignKey(
        GeographicDiv, to_field='tsn', on_delete=models.CASCADE)
    expert_id = models.ForeignKey(Expert, on_delete=models.CASCADE)

    def __str__(self):
        return f"geographic_tsn: {self.geographic_tsn}, expert_id: {self.expert_id}"


class SynonymLink(models.Model):
    # FIXME: Couldn't get this to work with two FKs with both pointing to
    # tsn column in TaxonomicUnit table
    tsn = models.IntegerField()
    tsn_accepted = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)
    update_date = models.DateTimeField()

    def __str__(self):
        return "tsn: {}, tsn_accepted: {}, update_date: {}".format(
            self.tsn,
            self.tsn_accepted,
            self.update_date
        )


try:
    from django.conf import settings
    ADS_TOKEN = settings.ADS_TOKEN
except (ImportError, AttributeError):
    ADS_TOKEN = ''

class RefError(Exception):
    pass
class UnresolvedDOIError(RefError):
    pass
class ADSError(RefError):
    pass

class Reference(models.Model):
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
        app_label = 'refs'


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


    @classmethod
    def get_ref_from_doi(cls, doi, query_ads=True):
        citeproc_json = get_citeproc_json_from_doi(doi)
        ref = parse_citeproc_json(citeproc_json, None, query_ads)
        return ref

# Here are some utility functions for obtaining Ref objects from external
# sources and parsing different bibliographic formats.

def get_citeproc_authors(cpd_author):
    if cpd_author is None:
        return None
    names = []
    for author in cpd_author:
        try:
            family = author['family'].title()
        except KeyError:
            # Occasionally an author isn't a single person,
            # e.g. "JET contributors", so do what we can here:
            name = author['name']
            names.append(name)
            continue
        try:
            given = author['given']
        except KeyError:
            # This author has first name
            names.append(family)
            continue
        initials = given.split()
        initials[0] = '{}.'.format(initials[0][0])
        initials = ' '.join(initials)
        names.append('{} {}'.format(initials, family))
    return ', '.join(names)


def get_bibcode(doi):
    url = requests.get('https://api.adsabs.harvard.edu/v1/search/query',
                       params={'q': 'doi:"{}"'.format(doi),
                               'fl': '*', 'rows': 2000},
                       headers={'Authorization': 'Bearer ' + ADS_TOKEN})
    ads_json = json.loads(url.text)
    if 'error' in ads_json:
        raise ADSError('ADS returned error: {}'.format(ads_json['error']))

    #if 'responseHeader' not in ads_json:
    #    print(ads_json)

    ads_response_status = ads_json['responseHeader']['status']
    if ads_response_status != 0:
        raise ADSError('ADS returned status {}'.format(ads_response_status))

    ads_response = ads_json.get('response', '')
    try:
        bibcode = ads_response['docs'][0]['bibcode']
    except IndexError:
        return None
    return bibcode


def get_title_from_bibcode(bibcode, fmt='html'):
    s_format_dict = r'%T'
    if fmt == 'latex':
        s_format_dict = r'%ZEncoding:latex %T'
    payload = {'bibcode': [bibcode],
               'sort': 'first_author asc',
               'format': s_format_dict
              }
    # POST our request, with retries (which must be explicitly allowed in
    # method_whitelist) on 502: Bad Gateway, 503: Service Unavailable and
    # 504: Gateway Timeout
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=0.5,
                    status_forcelist=[502, 503, 504],
                    method_whitelist=frozenset(['GET', 'POST']))
    s.mount('https://', HTTPAdapter(max_retries=retries))
    r = s.post('https://api.adsabs.harvard.edu/v1/export/custom',
                      headers={'Authorization': 'Bearer ' + ADS_TOKEN,
                               'Content-type': 'application/json'},
                      data=json.dumps(payload),
                     )
    if not r:
        raise ADSError('Bad response from ADS service: {}'.format(r))
    response_json = r.json()
    if 'error' in response_json:
        raise ADSError('ADS service returned an error: {}'
                             .format(response_json['error']))
    try:
        title = response_json['export']
    except KeyError:
        title = ''
    return title


def parse_citeproc_json(citeproc_json, ref=None, query_ads=True):
    """Parse the provided JSON into a Ref object."""

    cpd = json.loads(citeproc_json)
    # We only understand journal articles, for now.
    if cpd['type'] not in ('article-journal', 'journal-article'):
        raise NotImplementedError

    authors = get_citeproc_authors(cpd.get('author', ''))
    title = cpd.get('title', '')
    if title:
        title = title.replace('\n', ' ')
    journal = cpd.get('container-title', '')
    volume = cpd.get('volume', '')
    page_start, page_end = cpd.get('page', ''), ''
    if page_start:
        if '--' in page_start:
            page_start, page_end = page_start.split('--')
        else:
            # for an odd number of hyphens, split on the middle one
            nhyphens = page_start.count('-')
            if nhyphens % 2:
                f = page_start.split('-')
                page_start = '-'.join(f[:nhyphens//2+1])
                page_end = '-'.join(f[nhyphens//2+1:])
            
    article_number = cpd.get('article-number', '')
    doi = cpd.get('DOI', '')
    url = ensure_https(cpd.get('URL', ''))
    try:
        year = cpd['issued']['date-parts'][0][0]
    except (KeyError, IndexError):
        year = None

    if ref:
        ref.authors = authors
        ref.title = title
        ref.journal = journal
        ref.volume = volume
        ref.year = year
        ref.page_start = page_start
        ref.page_end = page_end
        ref.doi = doi
        ref.url = url
        ref.article_number = article_number
        ref.citeproc_json = citeproc_json
    else:
        ref = Ref(authors=authors, title=title, journal=journal, volume=volume,
                  year=year, page_start=page_start, page_end=page_end, doi=doi,
                  url=url, article_number=article_number,
                  citeproc_json=citeproc_json)

    if query_ads:
        bibcode = get_bibcode(doi)
        if bibcode:
            ref.bibcode = bibcode
            title_html = get_title_from_bibcode(bibcode)
            if title_html:
                ref.title_html = title_html
            title_latex = get_title_from_bibcode(bibcode, fmt='latex')
            if title_latex:
                ref.title_latex = title_latex
    return ref 

def get_citeproc_json_from_doi(doi):
    base_url = 'https://doi.org/'
    url = base_url + doi
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/citeproc+json')
    try:
        with urllib.request.urlopen(req) as f:
            citeproc_json = f.read().decode()
    except HTTPError as e:
        if e.code == 404:
            raise UnresolvedDOIError('DOI not found.')
        raise RefError
    return citeproc_json

def get_ref_from_doi(doi, ref=None, query_ads=True):
    citeproc_json = get_citeproc_json_from_doi(doi)
    ref = parse_citeproc_json(citeproc_json, ref, query_ads)
    return ref
