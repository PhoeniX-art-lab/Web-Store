from django.urls import path
from store.views import index, about, support, login, show_info, show_categories, success_view

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("support/", support, name='support'),
    path("support/success/", success_view, name='success'),
    path("login/", login, name='login'),
    path("information/<slug:info_slug>/", show_info, name='information'),
    path("categories/<slug:cat_slug>/", show_categories, name='categories'),
]
