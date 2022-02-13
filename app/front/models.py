from django.db import models # pylint:disable=W0611


# Create your models here.
class Kingdom(models.Model):
    """ Defines a kingdom """
    kingdom_name = models.CharField(max_length=100)
    update_date = models.DateTimeField()

class TaxonUnitType(models.Model):
    kingdom_id = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    rank_id = models.IntegerField(default=0)
    rank_name = models.CharField(max_length=100)
    dir_parent_rank_id = models.IntegerField(default=0)
    req_parent_rank_id = models.IntegerField(default=0)
    update_date = models.DateTimeField()


