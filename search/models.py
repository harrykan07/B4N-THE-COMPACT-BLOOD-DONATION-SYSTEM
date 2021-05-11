from dreg.models import DonorList
from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField

# data table for search logo
class SearchLogo(models.Model):
    title = models.CharField(blank=True, null=True, max_length=10)
    logo_number = models.IntegerField(blank=True, null=True)
    logo_image = models.ImageField(upload_to='logo')
    def __str__(self):
        return self.title

class RequestedRecord(models.Model):
    #id primary key automatically created
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
    units = models.IntegerField()
    location = LocationField(blank=True, null=True, map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", "center": (77.21987228649732,28.630981392199445)})
    address = AddressAutoHiddenField(blank=True, null=True)
    contact_number = models.CharField(max_length=10)
    # date = models.DateField(auto_now=True)
    emergency_choices=[
        ('urgently_required',"Urgently Required"),
        ("pick_a_date","Pick a date"),
    ]
    emergency = models.CharField(
        max_length=18, blank=True, null=True,
        choices=emergency_choices,
        )
    required_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    status = models.CharField(blank=True, null=True,max_length=10)
    def __str__(self):
        return str(self.id)

class Points(models.Model):
    donor_id = models.ForeignKey(DonorList,on_delete=models.CASCADE)
    req_id = models.ForeignKey(RequestedRecord,on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return str(self.id) + " donor is " + str(self.donor_id.id) + " req is " + str(self.req_id.id) + " having points " + str(self.points)

# class Friends(models.Model):
#     donor_id = models.ForeignKey(DonorList,on_delete=models.CASCADE)
#     friends_list = models.ManyToManyField(DonorList)