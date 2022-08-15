from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

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


def show_categories(request: Any, cat_id: int) -> HttpResponse:
    context = {
        'title': 'Camera Drones' if cat_id == 1 else 'Handheld',
        # 'menu': menu,
        'cat_selected': cat_id
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


def show_info(request: Any, info_id) -> HttpResponse:
    return HttpResponse(f"Page with id = {info_id}")


def pageNotFound(request: Any, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>404 Not Found Error</h1>")


def serverError(request: Any) -> HttpResponseServerError:
    return HttpResponseServerError("<h1>505 Server Error</h1>")
