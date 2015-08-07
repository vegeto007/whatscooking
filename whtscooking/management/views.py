import hashlib
import copy

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import FormUserRatings
from .models import UserRating, Vendor, VendorMenu


class Home(TemplateView):
    template_name = "index.html"


class Vendors(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Vendors, self).get_context_data(**kwargs)
        vendor_dict = {}
        for vendor in Vendor.objects.all():
            vendor_dict[vendor.name] = vendor.vendormenu_set.all()
        context['vendors'] = vendor_dict
        return context


class UserRatings(FormView):
    template_name = "user_rating.html"
    form_class = FormUserRatings
    success_url = '/rating/'

    def _save_info(self):
        vendor_id = self.request.POST['vendor']
        rating_id = self.request.POST['rating']
        user_agent = self.request.META['HTTP_USER_AGENT']
        remote_ip = self.request.META.get('REMOTE_ADDR')
        user_hash = hashlib.sha1(remote_ip + user_agent).hexdigest()
        vendor = Vendor.objects.get(id=vendor_id)
        user_rate, created = UserRating.objects.get_or_create(
            md5=user_hash)

        if created:
            user_rate.rating=rating_id
            user_rate.vendor_id=vendor
            status = 2
            message = 'You are already done with rating'
        else:
            user_rate.why = self.request.POST.get('why', '')
            user_rate.imp = self.request.POST.get('imp', '')
            status = 1
            message = 'Thanks For the rating, Its saved in our Database sucessfully'
        user_rate.save()
        return {'status': status, 'message': message}

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        data = self._save_info()
        self.request.session['data'] = data
        return super(UserRatings, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserRatings, self).get_context_data(**kwargs)
        user_rating_dict = self._process_user_rating()
        context.update(self.request.session.get('data', {}))
        context['user_rating_dict'] = user_rating_dict
        return context

    def _process_user_rating(self):
        """
        Process User Rating
        :return: user_rating_dict
        """
        user_rating_dict = {}
        user_rating_inner_dict = {'rating_super_like': 0,
                                  'rating_like': 0,
                                  'rating_not_like': 0}
        for vendor in Vendor.objects.all():
            user_rating_dict[vendor.name] = copy.copy(user_rating_inner_dict)

        for vendor in Vendor.objects.all():
            for user_rating in UserRating.objects.all():
                if user_rating.rating == '1':
                    user_rating_dict[vendor.name]['rating_super_like'] += 1
                elif user_rating.rating == '2':
                    user_rating_dict[vendor.name]['rating_like'] += 1
                elif user_rating.rating == '3':
                    user_rating_dict[vendor.name]['rating_not_like'] += 1

        return user_rating_dict
