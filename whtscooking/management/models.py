from django.db import models
from django.db.models import Count
from model_utils.models import TimeStampedModel
from model_utils import Choices

# Create your models here.


class Vendor(TimeStampedModel):
    id = models.CharField(max_length=10, verbose_name="Vendor ID", primary_key=True)
    name = models.CharField(max_length=30, verbose_name="Vendor Name")

    def __unicode__(self):
        return u'%s' % self.name


class VendorMenu(TimeStampedModel):
    item_id = models.CharField(max_length=10, verbose_name="Item ID")
    vendor_id = models.ForeignKey(Vendor, verbose_name="Vendor ID")
    item_name = models.CharField(max_length=30, verbose_name="Item Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Price")

    class Meta:
        unique_together = ('item_id', 'vendor_id')


class UserRating(TimeStampedModel):
    md5 = models.CharField(max_length=50, verbose_name="md5", primary_key=True)
    vendor_id = models.ForeignKey(Vendor, verbose_name="Vendor ID")
    rating_type = Choices(('1', 'Good'),
                          ('2', 'Average'),
                          ('3', 'Bad'), )
    rating = models.CharField(choices=rating_type,
                              max_length=10,
                              verbose_name='Rating')
    why = models.CharField(max_length=255, blank=True, null=True)
    imp = models.CharField(max_length=255, blank=True, null=True)