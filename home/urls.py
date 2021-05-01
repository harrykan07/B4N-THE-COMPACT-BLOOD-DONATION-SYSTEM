from django.urls import path
from .views import *

urlpatterns = [
    path('', homedisplay, name='homesite1'),
    path('loginland/', loginland, name='loginland'),


]
