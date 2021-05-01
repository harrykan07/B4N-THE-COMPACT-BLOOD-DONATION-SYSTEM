from django.shortcuts import render
from .models import HomePageSlider, HomePageBody


def loginland(request):
    return render(request, 'registration/afterlogin.html')


def homedisplay(request):
    home_slider = HomePageSlider.objects.get(id_number=1)
    our_vision = HomePageBody.objects.get(id_vision=1)
    donor_opinion = HomePageBody.objects.get(id_vision=2)
    user_opinion = HomePageBody.objects.get(id_vision=3)
    
    

    context = {
        'home_slider' : home_slider,
        'our_vision' : our_vision,
        'donor_opinion' : donor_opinion,
        'user_opinion' : user_opinion,
    }

    return render(request, 'home.html', context)


