from django.contrib import admin
from .models import Vendor, VendorMenu, Rating

# Register your models here.


class VendorAdmin(admin.ModelAdmin):

    model = Vendor
    list_display = ('id', 'name')


class VendorMenuAdmin(admin.ModelAdmin):

    model = VendorMenu
    list_display = ('item_id', 'vendor_id', 'item_name', 'description')


class RatingAdmin(admin.ModelAdmin):

    model = Rating
    list_display = ('md5', 'vendor_id', 'rating')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorMenu, VendorMenuAdmin)
admin.site.register(Rating, RatingAdmin)

