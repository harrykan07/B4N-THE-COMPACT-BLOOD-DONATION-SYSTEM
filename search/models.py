from dreg.forms import DonorRegistration
from dreg.models import DonorList
from django.db import models

# data table for search logo
class SearchLogo(models.Model):
    title = models.CharField(blank=True, null=True, max_length=10)
    logo_number = models.IntegerField(blank=True, null=True)
    logo_image = models.ImageField(upload_to='logo')
    def __str__(self):
        return self.title

class RequestedRecord(models.Model):
    #id primary key automatically created
    addr = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=10)
    units = models.IntegerField()
    date = models.DateField(auto_now=True)

class Points(models.Model):
    donor_id = models.ForeignKey(DonorList,on_delete=models.CASCADE)
    req_id = models.ForeignKey(RequestedRecord,on_delete=models.CASCADE)
    points = models.IntegerField()

# class Friends(models.Model):
#     donor_id = models.ForeignKey(DonorList,on_delete=models.CASCADE)
#     friends_list = models.ManyToManyField(DonorList)