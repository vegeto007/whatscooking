from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import FormUserRatings
from .models import UserRating


class Home(TemplateView):
    template_name = "index.html"


class UserRatings(FormView):
    template_name = "home.html"
    form_class = FormUserRatings
    success_url = '/rating/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super(UserRatings, self).form_valid(form)