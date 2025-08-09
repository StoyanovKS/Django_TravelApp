from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-trips/", views.all_trips, name="all_trips"),
    path("trips/create/", views.trip_create, name="trip_create"),
    path("trips/<int:pk>/details/", views.trip_details, name="trip_details"),
    path("trips/<int:pk>/edit/", views.trip_edit, name="trip_edit"),
    path("trips/<int:pk>/delete/", views.trip_delete, name="trip_delete"),
]
