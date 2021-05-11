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
            'emergency' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
<<<<<<< HEAD
            'required_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
=======
            'required_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
>>>>>>> e31fa913a993ec4378227d496ef2a2367df8a3c3
        }
        exclude = ['status']

