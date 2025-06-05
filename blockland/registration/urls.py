from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("land_registration/", views.land_registration, name="land_registration"),
]