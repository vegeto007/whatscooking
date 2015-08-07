from django.forms import ModelForm, Textarea
from django import forms
from .models import UserRating, Vendor, VendorMenu


class FormUserRatings(forms.Form):
    vendor = forms.ChoiceField(widget=forms.RadioSelect, choices=[(obj.id, obj.name) for obj in Vendor.objects.all()])
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=UserRating.rating_type)

class VendorMenuForm(forms.Form):
    vendor_id = forms.ChoiceField(choices=[(obj.id, obj.name) for obj in Vendor.objects.all()])

    class Meta:
        model = VendorMenu
        fields = ('vendor_id', )