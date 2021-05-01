from django import forms


class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select blood group"),
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
    )
    select_blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )

    select_location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'Hospital Address?..e.g..binalbagan'
            }
        ),
    )
    mobile_no = forms.CharField(
        label="Contact Number",
        max_length=10,
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'Enter your contact number'
            }
        ),
    )
    city = forms.CharField(
        label="City",
        max_length=10,
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'Enter City Name'
            }
        ),
    )
    units = forms.IntegerField(
        label="Units of blood",
        widget=forms.NumberInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'Enter Units of blood needed'
            }
        ),
    )

