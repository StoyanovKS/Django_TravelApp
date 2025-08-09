from django import forms
from .models import Trip

class TripCreateForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ["traveler"]  # set in the view
        widgets = {
            "destination": forms.TextInput(attrs={"placeholder": "Enter a short destination note..."}),
            "summary": forms.Textarea(attrs={"placeholder": "Share your exciting moments...", "rows": 8}),
            "image_url": forms.URLInput(attrs={"placeholder": "An optional image URL..."}),
        }

class TripEditForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ["traveler"]

class TripDeleteForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ["destination", "summary", "start_date", "duration", "image_url"]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 8}),
        }

    # make fields read-only in the template by checking form.fields
