from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, FormView, DetailView

from .forms import SupportForm
from .models import Store, Category
from .utils import DataMixin


class HomeStore(DataMixin, ListView):
    model = Store
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeStore, self).get_context_data(**kwargs)
        data_context = self.get_user_context(title='Dji Store')
        return context | data_context


class CategoriesStore(DataMixin, ListView):
    model = Store
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesStore, self).get_context_data(**kwargs)
        data_context = self.get_user_context(
            title='Camera Drones' if self.kwargs['cat_slug'] == 'camera-drones' else 'Handheld',
            cat_selected=Category.objects.get(slug=self.kwargs['cat_slug']).pk)
        return context | data_context


def about(request: Any) -> HttpResponse:
    return render(request, 'store/about.html', context={'title': 'About'})


class SupportStore(DataMixin, FormView):
    form_class = SupportForm
    template_name = 'store/support.html'
    success_url = 'success'

    def get_context_data(self, **kwargs):
        context = super(SupportStore, self).get_context_data(**kwargs)
        data_context = self.get_user_context(title='Support')
        return context | data_context

    def form_valid(self, form):
        issue_type = form.cleaned_data['issue_type']
        email = form.cleaned_data['email']
        text = form.cleaned_data['text']
        send_mail(f'{issue_type} from {email}', text, settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
        return super(SupportStore, self).form_valid(form)


def success_view(request: Any) -> HttpResponse:
    return HttpResponse("Thank you for your request, we will reply to you soon")


def login(request: Any) -> HttpResponse:
    return render(request, 'store/login.html', context={'title': 'Login'})


class InformationStore(DataMixin, DetailView):
    model = Store
    template_name = 'store/object_information.html'
    slug_url_kwarg = 'info_slug'
    context_object_name = 'information'

    def get_context_data(self, **kwargs):
        context = super(InformationStore, self).get_context_data(**kwargs)
        data_context = self.get_user_context(title=context['information'])
        return context | data_context


def pageNotFound(request: Any, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>404 Not Found Error</h1>")


def serverError(request: Any) -> HttpResponseServerError:
    return HttpResponseServerError("<h1>505 Server Error</h1>")
