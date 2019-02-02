from django import forms
from .models import TrucksData


class TrucksSubmit(forms.ModelForm):
    truck_number = forms.CharField(
        widget=forms.TextInput(), required=True, max_length=14)
    insurance_number = forms.IntegerField(widget=forms.NumberInput())
    insurance_expiry = forms.DateField(required=True)
    fitness_certificate_id = forms.CharField(
        widget=forms.TextInput(), required=True)
    fitness_certificate_expiry = forms.DateField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = TrucksData
        fields = '__all__'
