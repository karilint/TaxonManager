from django.db import models # pylint:disable=W0611


# Create your models here.
class Kingdom(models.Model):
    """ Defines a kingdom """
    kingdom_name = models.CharField(max_length=100)
    update_date = models.DateTimeField()

class TaxonUnitType(models.Model):
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(default=0)
    rank_name = models.CharField(max_length=100)
    dir_parent_rank_id = models.IntegerField(default=0)
    req_parent_rank_id = models.IntegerField(default=0)
    update_date = models.DateTimeField()

class TaxonomicUnit(models.Model):
    # TODO: Add tsn if required
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
    # TODO: Mistä tsn tulee?
    parent_tsn = models.IntegerField(default=0)
    taxon_author_id = models.IntegerField(default=0)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(default=0)
    hybrid_author_id = models.IntegerField(default=0)
    update_date = models.DateTimeField()
    uncertain_prnt_ind = models.CharField(max_length=100)
    n_usage = models.CharField(max_length=100)
    complete_name = models.CharField(max_length=100)

    def __str__(self):
        return self.id