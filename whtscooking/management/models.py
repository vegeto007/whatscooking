from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices

# Create your models here.


class Vendor(TimeStampedModel):
    id = models.CharField(max_length=10, verbose_name="Vendor ID", primary_key=True)
    name = models.CharField(max_length=30, verbose_name="Vendor Name")


class VendorMenu(TimeStampedModel):
    item_id = models.CharField(max_length=10, verbose_name="Item ID")
    vendor_id = models.ForeignKey(Vendor, verbose_name="Vendor ID")
    item_name = models.CharField(max_length=30, verbose_name="Item ID")
    description = models.TextField(verbose_name="Description")

    class Meta:
        unique_together = ('item_id', 'vendor_id')


class Rating(TimeStampedModel):
    md5 = models.CharField(max_length=50, verbose_name="md5", primary_key=True)
    vendor_id = models.ForeignKey(Vendor, verbose_name="Vendor ID")
    rating_type = Choices(('1', 'Good'),
                          ('2', 'Average'),
                          ('3', 'Bad'), )
    rating = models.CharField(choices=rating_type,
                              max_length=10,
                              verbose_name='Rating')


