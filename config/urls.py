from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("trips.urls")),         # index + trips + all-trips
    path("traveler/", include("travelers.urls")),
]
