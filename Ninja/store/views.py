from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, FormView, DetailView

from .forms import SupportForm
from .models import Store, Category

menu = [{"title": "Login", "url_name": "login"},
        {"title": "Support", "url_name": "support"},
        {"title": "About", "url_name": "about"}]


class HomeStore(ListView):
    model = Store
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeStore, self).get_context_data(**kwargs)
        context['title'] = 'Dji Store'
        context['cat_selected'] = None
        return context


class CategoriesStore(ListView):
    model = Store
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesStore, self).get_context_data(**kwargs)
        context['title'] = 'Camera Drones' if self.kwargs['cat_slug'] == 'camera-drones' else 'Handheld'
        context['cat_selected'] = Category.objects.get(slug=self.kwargs['cat_slug']).pk
        return context


def about(request: Any) -> HttpResponse:
    return render(request, 'store/about.html', context={'title': 'About'})


class SupportStore(FormView):
    form_class = SupportForm
    template_name = 'store/support.html'
    success_url = 'success'

    def get_context_data(self, **kwargs):
        context = super(SupportStore, self).get_context_data(**kwargs)
        context['title'] = 'Support'
        return context

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


class InformationStore(DetailView):
    model = Store
    template_name = 'store/object_information.html'
    slug_url_kwarg = 'info_slug'
    context_object_name = 'information'

    def get_context_data(self, **kwargs):
        context = super(InformationStore, self).get_context_data(**kwargs)
        context['title'] = context['information']
        return context


def pageNotFound(request: Any, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>404 Not Found Error</h1>")


def serverError(request: Any) -> HttpResponseServerError:
    return HttpResponseServerError("<h1>505 Server Error</h1>")
