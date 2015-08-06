from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import FormUserRatings
from .models import UserRating, Vendor, VendorMenu


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        vendor_dict = {}
        for vendor in Vendor.objects.all():
            vendor_dict[vendor.name] = vendor.vendormenu_set.all()
        context['vendors'] = vendor_dict
        return context


class UserRatings(FormView):
    template_name = "home.html"
    form_class = FormUserRatings
    success_url = '/rating/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(UserRatings, self).form_valid(form)