from django import forms
from .models import Traveler

class TravelerCreateForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ["nickname", "email", "country"]
        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "Enter a unique nickname..."}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter a valid email address..."}),
            "country": forms.TextInput(attrs={"placeholder": "Enter a country code like <BGR>..."}),
        }

class TravelerEditForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ["nickname", "email", "country", "about_me"]
        widgets = {
            "about_me": forms.Textarea(attrs={"rows": 6}),
        }
