from django.urls import path
from .views import donorregdisplay
#, donorregsuccess

urlpatterns = [
    path('', donorregdisplay, name='dregsite'),
    path('donors', donorregdisplay, name='dregdisplay')
]