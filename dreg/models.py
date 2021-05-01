from django.db import models


#Donor resistration forms data table
class DonorList(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    date_of_birth = models.DateField(blank=True, null=True)
    blood_choices=[
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),

    ]
    blood_group = models.CharField(
        max_length=4, blank=True, null=True,
        choices=blood_choices
        )
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    occupation = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    last_donate_date = models.CharField(max_length=50, blank=True, null=True)
    any_diseases_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    any_diseases = models.CharField(
        max_length=4, blank=True, null=True,
        choices=any_diseases_choices,
        )
    allergies_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    allergies = models.CharField(
        max_length=4, blank=True, null=True,
        choices=allergies_choices,
        )
    cardiac_choices=[
        ("yes","Yes"),
        ("no", "No"),
    ]
    cardiac = models.CharField(
        max_length=4, blank=True, null=True,
        choices=cardiac_choices,
        )
    bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    bleeding_disorders = models.CharField(
        max_length=4, blank=True, null=True,
        choices=bleeding_disorders_choices,
        )
    hbsAg_hcv_hIV_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    hbsAg_hcv_hIV =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hbsAg_hcv_hIV_choices,
        )
    willing_to_donate_plasma_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    willing_to_donate_plasma = models.CharField(
        max_length=4, blank=True, null=True,
        choices=willing_to_donate_plasma_choices,
        )



    def __str__(self):
        return self.name



