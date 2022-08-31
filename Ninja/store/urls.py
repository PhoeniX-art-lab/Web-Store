from django.urls import path
from store.views import *

urlpatterns = [
    path("", HomeStore.as_view(), name='home'),
    path("about/", about, name='about'),
    path("support/", SupportStore.as_view(), name='support'),
    path("support/success/", success_view, name='success'),
    path("login/", LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path("register/", UserRegistration.as_view(), name='register'),
    path("information/<slug:info_slug>/", InformationStore.as_view(), name='information'),
    path("categories/<slug:cat_slug>/", CategoriesStore.as_view(), name='categories'),
]
