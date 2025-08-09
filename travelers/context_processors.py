from travelers.models import Traveler

def has_profile(request):
    return {"has_profile": Traveler.objects.exists()}
