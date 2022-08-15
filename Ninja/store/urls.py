from django.urls import path
from store.views import index, about, support, login, show_info, show_categories

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("support/", support, name='support'),
    path("login/", login, name='login'),
    path("information/<int:info_id>/", show_info, name='information'),
    path("categories/<int:cat_id>/", show_categories, name='categories'),
]
