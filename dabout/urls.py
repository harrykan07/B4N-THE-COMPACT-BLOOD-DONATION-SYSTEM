from django.urls import path
from .views import aboutdisplay

urlpatterns = [
    path('', aboutdisplay, name='aboutsite1'),
]

