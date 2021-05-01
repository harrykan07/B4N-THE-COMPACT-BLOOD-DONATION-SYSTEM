from django.shortcuts import render
from .models import ContactPageBody

def contactdisplay(request):
    contact = ContactPageBody.objects.get(id_contact=1)
    context = {
        'contact' : contact
    }
    return render(request, 'contact_us.html', context)
