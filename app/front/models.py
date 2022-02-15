from django.db import models # pylint:disable=W0611
import uuid
from django.utils import timezone

class Comment(models.Model):
    commentator = models.CharField(max_length=200)
    comment_detail = models.TextField()
    comment_time_stamp = models.DateTimeField()
    update_date = models.DateTimeField()

# Create your models here.
class Kingdom(models.Model):
    """ Defines a kingdom """
    kingdom_name = models.CharField(max_length=100, blank=False)
    update_date = models.DateTimeField()

class TaxonUnitType(models.Model):
    class Meta:
        unique_together = (('kingdom', 'rank_id'))

    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(default=0)
    rank_name = models.CharField(max_length=100)
    dir_parent_rank_id = models.IntegerField(default=0)
    req_parent_rank_id = models.IntegerField(default=0)
    update_date = models.DateTimeField()

    def __str__(self):
        return "Kingdom: {}, rank_id:{}, rank_name:{}, dir_parent_rank_id:{}".format(
            self.kingdom,
            self.rank_id,
            self.rank_name,
            self.dir_parent_rank_id
        )
    
class TaxonAuthorLkp(models.Model):
    class Meta:
        unique_together = (('taxon_author_id', 'kingdom_id'))

    taxon_author_id = models.IntegerField(primary_key=True) #models.ForeignKey(TaxonomicUnit, to_field='taxon_author_id', on_delete=models.CASCADE)
    taxon_author = models.CharField(max_length=100)
    update_date = models.DateTimeField()
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    short_author = models.CharField(max_length=50)

class TaxonomicUnit(models.Model):
    """
    Taxonomic Units
    """
    tsn = models.AutoField(primary_key=True)
    unit_ind1 = models.CharField(max_length=100)
    unit_name1 = models.CharField(max_length=100)
    unit_ind2 = models.CharField(max_length=100)
    unit_name2 = models.CharField(max_length=100)
    unit_ind3 = models.CharField(max_length=100)
    unit_name3 = models.CharField(max_length=100)
    unit_ind4 = models.CharField(max_length=100)
    unnamed_taxon_ind = models.CharField(max_length=100)
    name_usage = models.CharField(max_length=100)
    unaccept_reason = models.CharField(max_length=100)
    credibility_rtng = models.CharField(max_length=100)
    completeness_rtng = models.CharField(max_length=100)
    currency_rating = models.CharField(max_length=100)
    phylo_sort_seq = models.IntegerField(default=0)
    initial_time_stamp = models.DateTimeField()
    parent_tsn = models.IntegerField(default=0)
    taxon_author_id = models.ForeignKey(TaxonAuthorLkp, on_delete=models.CASCADE)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(default=0)
    hybrid_author_id = models.IntegerField(default=0)
    update_date = models.DateTimeField()
    uncertain_prnt_ind = models.CharField(max_length=100)
    n_usage = models.CharField(max_length=100)
    complete_name = models.CharField(max_length=100)
    
    # Relationships
    comments = models.ManyToManyField(
        'Comment', through='TuCommentLink'
    )

    def __str__(self):
        return self.id

class Hierarchy(models.Model):
    """
    Describes hierarchies, I guess?
    """
    hierarchy_string = models.CharField(max_length=300)
    tsn = models.ForeignKey(TaxonomicUnit,on_delete=models.CASCADE) # models.IntegerField(null=True)#
    parent_tsn = models.IntegerField(default=0)
    level =  models.IntegerField()
    childrencount = models.IntegerField(default=0)

class TuCommentLink(models.Model):
    """
    Many-to-many table between Comment and TaxonomicUnit tables
    """
    tsn = models.ForeignKey(TaxonomicUnit,on_delete=models.CASCADE) # models.IntegerField(null=True)#
    comment_id = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )
    update_date = models.DateTimeField()

class Publication(models.Model):
    class Meta:
        unique_together = (('pub_id_prefix', 'publication_id')) 

    pub_id_prefix = models.CharField(max_length=3, unique=True)
    publication_id = models.IntegerField(primary_key=True)
    reference_author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    publication_name = models.CharField(max_length=255)
    listed_pub_date = models.DateTimeField()
    actual_pub_date = models.DateTimeField()
    publisher = models.CharField(max_length=80)
    pub_place = models.CharField(max_length=40)
    isbn = models.CharField(max_length=16)
    issn = models.CharField(max_length=40)
    pages = models.CharField(max_length=15)
    pub_comment = models.CharField(max_length=500)
    update_date = models.DateTimeField()
    
    def __repr__(self):
        return "Publication id: {self.publication_id}"

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
    documentation_id = models.ForeignKey(Publication, to_field='publication_id', on_delete=models.CASCADE)
    # TODO: made des desc for clarity. Change database schema to match!
    original_desc_ind = models.CharField(max_length=1)
    init_itis_desc_ind = models.CharField(max_length=1)
    change_track_id = models.IntegerField()
    vernacular_name = models.CharField(max_length=80)
    update_date = models.DateTimeField()

class Expert(models.Model):
    """ Database model of Experts table """
    # TODO: expert_id_prefix left out, this is a char field
    # that only contains EXP presumably for all rows.
    expert = models.CharField(max_length=100)
    exp_comment = models.CharField(max_length=500)
    update_date = models.DateTimeField()

    def __repr__(self):
        return "Expert name: {self.expert}"

class GeographicDiv(models.Model):
    class Meta:
        unique_together = (('tsn', 'geographic_value'))

    tsn = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE, unique=True)
    geographic_value = models.CharField(max_length=45)
    update_date = models.DateTimeField()

    # Relationship defining experts for a given geographical area
    experts = models.ManyToManyField(
        'Expert', through='ExpertsGeographicDiv'
    )

class ExpertsGeographicDiv(models.Model):
    # FIXME: Connecting the ExpertsGeographicDiv with TSN might not work
    # correctly to achieve many-to-many relationship between experts and
    # geographic areas. If we defined an ID to GeographicDiv table, this
    # may work better. This is just a hunch though.
    geographic_tsn = models.ForeignKey(GeographicDiv, to_field='tsn', on_delete=models.CASCADE)
    expert_id = models.ForeignKey(Expert, on_delete=models.CASCADE)

class SynonymLink(models.Model):
    # FIXME: Couldn't get this to work with two FKs with both pointing to
    # tsn column in TaxonomicUnit table
    tsn = models.IntegerField()
    tsn_accepted = models.ForeignKey(TaxonomicUnit, on_delete=models.CASCADE)
    update_date = models.DateTimeField()