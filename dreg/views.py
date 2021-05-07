from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import DonorRegistration
from .models import DonorList

#FOR MAPS
from django.views.generic import CreateView, UpdateView, ListView



class AddPlaceView(CreateView):
    model = DonorList
    template_name = "register.html"
    # success_url = "/index/"
    fields = ("location", "address")


# class ChangePlaceView(UpdateView):
#     model = DonorList
#     template_name = "live_demo/place_form.html"
#     success_url = "/index/"
#     fields = ("location", "address")


# class PlacesView(ListView):
#     model = DonorList
#     template_name = "live_demo/index.html"
#     ordering = ["-created_at", ]


#MAP END
#Donnor forms display
def donorregdisplay(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            donor = forms.save()
            password = forms.cleaned_data['password']
            email = forms.cleaned_data['email']
            name = forms.cleaned_data['name']
            user = User.objects.create_user(email, email, password)
            user.first_name = name
            user.last_name = donor.id
            user.save()
            print(forms.errors)
            context_details ={
                'forms' : forms
            }
            #After donor registation donor details display
            return render(request, 'registrations.html', context_details)

    context = {
                'forms' : forms,
            }

            
    return render(request, 'register.html', context)

