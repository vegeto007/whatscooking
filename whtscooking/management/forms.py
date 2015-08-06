from django.forms import ModelForm, Textarea
from django import forms
from .models import UserRating, Vendor


class FormUserRatings(ModelForm):
    Vendor = forms.ChoiceField(widget=forms.RadioSelect, choices=[(obj.id, obj.name) for obj in Vendor.objects.all()])
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=UserRating.rating_type)

    class Meta:
        model = UserRating
        fields = ('Vendor', 'rating')
