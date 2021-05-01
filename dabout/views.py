from django.shortcuts import render
from .models import AboutPageBody

def aboutdisplay(request):
    about = AboutPageBody.objects.get(id_about=1)
    context = {
        'about' : about,
    }
    return render(request, 'about_us.html', context)
