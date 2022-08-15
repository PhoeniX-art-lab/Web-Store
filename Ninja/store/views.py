from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404

from .models import Store, Category

menu = [{"title": "Login", "url_name": "login"},
        {"title": "Support", "url_name": "support"},
        {"title": "About", "url_name": "about"}]


def index(request: Any) -> HttpResponse:
    context = {
        'title': 'Dji Store',
        # 'menu': menu,
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
    # context = {
    #     'menu': menu
    # }
    return render(request, 'store/about.html', context=None)


def support(request: Any) -> HttpResponse:
    # context = {
    #     'menu': menu
    # }
    return render(request, 'store/support.html', context=None)


def login(request: Any) -> HttpResponse:
    # context = {
    #     'menu': menu
    # }
    return render(request, 'store/login.html', context=None)


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
