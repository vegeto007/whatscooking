from django.forms import ModelForm, Textarea
from django import forms

from .models import UserRating, Vendor


class FormUserRatings(forms.Form):
    vendor = forms.ChoiceField(widget=forms.RadioSelect, choices=[(obj.id, obj.name) for obj in Vendor.objects.all()])
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=UserRating.rating_type)