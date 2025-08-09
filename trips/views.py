from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from travelers.models import Traveler
from .models import Trip
from .forms import TripCreateForm, TripEditForm, TripDeleteForm

def index(request):
    return render(request, "index.html")

def all_trips(request):
    trips = Trip.objects.order_by("-start_date")
    return render(request, "all-trips.html", {"trips": trips})

def trip_create(request):
    traveler = Traveler.objects.first()
    if not traveler:
        return redirect("traveler_create")
    form = TripCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        trip = form.save(commit=False)
        trip.traveler = traveler
        trip.save()
        return redirect("all_trips")
    return render(request, "create-trip.html", {"form": form})

def trip_details(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, "details-trip.html", {"trip": trip})

def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    form = TripEditForm(request.POST or None, instance=trip)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("all_trips")
    return render(request, "edit-trip.html", {"form": form})

def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        trip.delete()
        return redirect("all_trips")
    form = TripDeleteForm(instance=trip)
    return render(request, "delete-trip.html", {"form": form})
