from django.contrib import admin
from .models import DonorList


class DonorListShow(admin.ModelAdmin):
    list_display = ['name', 'blood_group', 'home_address']


admin.site.register(DonorList, DonorListShow)
