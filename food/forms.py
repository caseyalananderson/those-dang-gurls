from django import forms
from .models import FoodEntry, Recipe

class FoodEntryForm(forms.ModelForm):

    class Meta:
        model = FoodEntry
        fields = ('content',)