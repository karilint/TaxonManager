from django.db import models # pylint:disable=W0611

# (null=True, blank=True) allows empty fields, makes testing easier for now

class Comment(models.Model):
    commentator = models.CharField(max_length=100)
    comment_detail = models.TextField(max_length=2000)
    comment_time_stamp = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

# Create your models here.
class Kingdom(models.Model):
    """ Defines a kingdom """
    kingdom_name = models.CharField(max_length=20)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Kingdom: {}".format(
            self.kingdom_name,
        )

class TaxonUnitType(models.Model):
    class Meta:
        unique_together = (('kingdom', 'rank_id'))

    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(null=True, blank=True)
    rank_name = models.CharField(max_length=100)
    dir_parent_rank_id = models.IntegerField(null=True, blank=True)
    req_parent_rank_id = models.IntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

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

    taxon_author_id = models.IntegerField(primary_key=True)
    taxon_author = models.CharField(max_length=100, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    short_author = models.CharField(max_length=50, null=True, blank=True)

class TaxonomicUnit(models.Model):
    """
    Taxonomic Units
    """
    tsn = models.AutoField(primary_key=True)
    unit_ind1 = models.CharField(max_length=1, null=True, blank=True)
    unit_name1 = models.CharField(max_length=35, null=True, blank=True)
    unit_ind2 = models.CharField(max_length=1, null=True, blank=True)
    unit_name2 = models.CharField(max_length=35, null=True, blank=True)
    unit_ind3 = models.CharField(max_length=7, null=True, blank=True)
    unit_name3 = models.CharField(max_length=35, null=True, blank=True)
    unit_ind4 = models.CharField(max_length=7, null=True, blank=True)
    unit_name4 = models.CharField(max_length=35, null=True, blank=True)
    unnamed_taxon_ind = models.CharField(max_length=100, null=True, blank=True)
    name_usage = models.CharField(max_length=100, null=True, blank=True)
    unaccept_reason = models.CharField(max_length=100, null=True, blank=True)
    credibility_rtng = models.CharField(max_length=100, null=True, blank=True)
    completeness_rtng = models.CharField(max_length=100, null=True, blank=True)
    currency_rating = models.CharField(max_length=100, null=True, blank=True)
    phylo_sort_seq = models.IntegerField(null=True, blank=True)
    initial_time_stamp = models.DateTimeField(null=True, blank=True)
    parent_tsn = models.IntegerField()
    taxon_author_id = models.ForeignKey(TaxonAuthorLkp, on_delete=models.CASCADE)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(null=True, blank=True)
    hybrid_author_id = models.IntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    uncertain_prnt_ind = models.CharField(max_length=100, null=True, blank=True)
    n_usage = models.CharField(max_length=100, null=True, blank=True)
    complete_name = models.CharField(max_length=100, null=True, blank=True)
    
    # Relationships
    comments = models.ManyToManyField(
        'Comment', through='TuCommentLink'
    )

    def __str__(self):
        return f"tsn_id: {self.tsn} parent_tsn: {self.parent_tsn}"

class Hierarchy(models.Model):
    """
    Describes hierarchies, I guess?
    """
    hierarchy_string = models.CharField(max_length=300, null=True, blank=True)
    tsn = models.ForeignKey(TaxonomicUnit,on_delete=models.CASCADE) # models.IntegerField(null=True)#
    parent_tsn = models.IntegerField(null=True, blank=True)
    level =  models.IntegerField(null=True, blank=True)
    childrencount = models.IntegerField(null=True, blank=True)

class TuCommentLink(models.Model):
    """
    Many-to-many table between Comment and TaxonomicUnit tables
    """
    tsn = models.ForeignKey(TaxonomicUnit,on_delete=models.CASCADE) # models.IntegerField(null=True)#
    comment_id = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )
    update_date = models.DateTimeField(null=True, blank=True)

class Publication(models.Model):
    class Meta:
        unique_together = (('pub_id_prefix', 'publication_id')) 

    pub_id_prefix = models.CharField(max_length=3, unique=True)
    publication_id = models.IntegerField(primary_key=True)
    reference_author = models.CharField(max_length=100,null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    publication_name = models.CharField(max_length=255,null=True, blank=True)
    listed_pub_date = models.DateTimeField(null=True, blank=True)
    actual_pub_date = models.DateTimeField(null=True, blank=True)
    publisher = models.CharField(max_length=80,null=True, blank=True)
    pub_place = models.CharField(max_length=40,null=True, blank=True)
    isbn = models.CharField(max_length=16,null=True, blank=True)
    issn = models.CharField(max_length=40,null=True, blank=True)
    pages = models.CharField(max_length=15,null=True, blank=True)
    pub_comment = models.CharField(max_length=500,null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    
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
    geographic_value = models.CharField(max_length=45, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

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