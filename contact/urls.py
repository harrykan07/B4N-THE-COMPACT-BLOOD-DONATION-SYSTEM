from django.urls import path
from .views import contactdisplay

urlpatterns = [
    path('', contactdisplay, name='contactsite1'),
]
