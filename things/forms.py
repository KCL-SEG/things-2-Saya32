"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.Form):
    name = forms.CharField(max_length=35, unique=True)
    description = forms.CharField(widget=forms.Textarea, blank=True)
    quantity = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )

    class Meta:
        exclude = ['created_at']