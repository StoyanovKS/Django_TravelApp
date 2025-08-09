from django.shortcuts import render, redirect, get_object_or_404
from .models import Traveler
from .forms import TravelerCreateForm, TravelerEditForm
from trips.models import Trip

def traveler_create(request):
    if Traveler.objects.exists():
        return redirect("all_trips")
    form = TravelerCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("all_trips")
    return render(request, "create-traveler.html", {"form": form})

def traveler_details(request):
    traveler = get_object_or_404(Traveler)
    trips = traveler.trips.order_by("-start_date")
    return render(request, "details-traveler.html", {"traveler": traveler, "trips": trips})

def traveler_edit(request):
    traveler = get_object_or_404(Traveler)
    form = TravelerEditForm(request.POST or None, instance=traveler)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("traveler_details")
    return render(request, "edit-traveler.html", {"form": form})

def traveler_delete(request):
    traveler = get_object_or_404(Traveler)
    if request.method == "POST":
        traveler.delete()
        return redirect("index")
    return render(request, "delete-traveler.html")
