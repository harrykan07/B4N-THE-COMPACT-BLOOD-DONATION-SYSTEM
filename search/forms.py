from django import forms
from django.forms import ModelForm
from .models import RequestedRecord


class DonorSearch(ModelForm):
    class Meta:
        model = RequestedRecord
        fields = '__all__'
        widgets = {
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'units' : forms.NumberInput(attrs={'class':'form-control','max':'20', 'required':'True'}),
            'contact_number' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
        }
        exclude = ['status']

