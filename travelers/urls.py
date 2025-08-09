from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.traveler_create, name="traveler_create"),
    path("details/", views.traveler_details, name="traveler_details"),
    path("edit/", views.traveler_edit, name="traveler_edit"),
    path("delete/", views.traveler_delete, name="traveler_delete"),
]
