from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import SupportForm
from .models import Store, Category

menu = [{"title": "Login", "url_name": "login"},
        {"title": "Support", "url_name": "support"},
        {"title": "About", "url_name": "about"}]


def index(request: Any) -> HttpResponse:
    context = {
        'title': 'Dji Store',
        'cat_selected': None
    }
    return render(request, 'store/index.html', context=context)


def show_categories(request: Any, cat_slug: str) -> HttpResponse:
    context = {
        'title': 'Camera Drones' if cat_slug == 'camera-drones' else 'Handheld',
        # 'menu': menu,
        'cat_selected': Category.objects.get(slug=cat_slug).pk
    }
    return render(request, 'store/index.html', context=context)


def about(request: Any) -> HttpResponse:
    return render(request, 'store/about.html', context={'title': 'About'})


def support(request: Any) -> HttpResponse:
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            issue_type = form.cleaned_data['issue_type']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            send_mail(f'{issue_type} from {email}', text, settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
            return redirect('success')
    else:
        form = SupportForm()

    return render(request, 'store/support.html', context={'form': form, 'title': 'Support'})


def success_view(request: Any) -> HttpResponse:
    return HttpResponse("Thank you for your request, we will reply to you soon")


def login(request: Any) -> HttpResponse:
    return render(request, 'store/login.html', context={'title': 'Login'})


def show_info(request: Any, info_slug: str) -> HttpResponse:
    information = get_object_or_404(Store, slug=info_slug)
    context = {
        'title': information.product_name,
        'information': information,
        'cat_selected': information.category_id
    }
    return render(request, 'store/object_information.html', context=context)


def pageNotFound(request: Any, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>404 Not Found Error</h1>")


def serverError(request: Any) -> HttpResponseServerError:
    return HttpResponseServerError("<h1>505 Server Error</h1>")
