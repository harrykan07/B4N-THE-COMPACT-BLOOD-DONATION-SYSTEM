from django.shortcuts import render
from .models import HomePageSlider, HomePageBody
from search .dashboardUtils import getDonationRecord, nextDonationDate


def loginland(request):
    details = getDonationRecord(request.user.last_name)
    nextDonation = nextDonationDate(request.user.last_name)
    print(nextDonation)
    context = {
        'donations' : details,
        'nextDonation' : nextDonation
    }
    return render(request, 'registration/afterlogin.html',context)


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


