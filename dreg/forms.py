from django import forms
from django.forms import ModelForm
from .models import DonorList

#Donor registrarion forms create
class DonorRegistration(ModelForm):
    class Meta:
        model = DonorList
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'home_address' : forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
            'last_donate_date' : forms.DateInput(attrs={'type': 'date'}),
            'any_diseases' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'allergies' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'cardiac' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'bleeding_disorders' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'hbsAg_hcv_hIV' : forms.Select(attrs={'class':'form-control', 'required':'True'}), 
            'willing_to_donate_plasma' : forms.Select(attrs={'class':'form-control', 'required':'True'}), 
        }
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter password used for login','required':'True'}
    ))
    exclude = ['donation_record']