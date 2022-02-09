from django.db import models # pylint:disable=W0611

# Create your models here.
class Reference(models.Model):
    authors         = models.CharField(max_length=80)
    year            = models.CharField(max_length=4)
    edition         = models.CharField(max_length=10)
    volume          = models.CharField(max_length=10)
    no_of_pages     = models.CharField(max_length=20)
    publisher       = models.CharField(max_length=20)
    city            = models.CharField(max_length=15)
    title           = models.CharField(max_length=30)
    journal         = models.CharField(max_length=200)
    bookTitle       = models.CharField(max_length=200)
    referenceType   = models.CharField(max_length=200)

    # Probably needs some kind of 