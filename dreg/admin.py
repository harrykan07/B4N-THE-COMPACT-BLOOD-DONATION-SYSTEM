from django.contrib import admin
from .models import DonorList
# from mapbox_location_field.admin import MapAdmin 


class DonorListShow(admin.ModelAdmin):
    list_display = ['name', 'blood_group']


admin.site.register(DonorList, DonorListShow)

# admin.site.register(MapAdmin)