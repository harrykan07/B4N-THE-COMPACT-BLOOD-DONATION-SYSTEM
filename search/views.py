import threading
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DonorSearch
from dreg.models import DonorList
from .models import SearchLogo
from .models import Points
from .models import RequestedRecord
from .NotifyDonor import notify_donor
from django.core.files.storage import FileSystemStorage
from .dashboardUtils import getDonationRecord

#FOR MAPS
from django.views.generic import CreateView



class AddPlaceView(CreateView):
    model = RequestedRecord
    template_name = "search.html"
    # success_url = "/index/"
    fields = ("location", "address")

def searchdisplay(request):
    forms = DonorSearch()
    logo_img = SearchLogo.objects.get(logo_number=1)
    if request.method == 'POST':
        forms = DonorSearch(request.POST)
        if forms.is_valid():
            notify_donor(forms.cleaned_data,forms)
            return render(request,'reqAccepted.html')
        else:
            return render(request,'errorPage.html')

    context = {
        'forms_search' : forms,
        'logo_img' : logo_img
    }
    return render(request, 'search.html' ,context)

def donorlistdetail(request, email):
    email = email
    detail = DonorList()
    detail = DonorList.objects.get(email=email)
    context = {
        'details' : detail
    }
    return render(request, 'information.html', context)


# @login_required
def donorupdate(request, cid):
    detail = Points.objects.get(pk=cid)
    req = detail.req_id
    if req.status == "donor":
        return render(request, 'donorAccepted.html')
    elif req.status == "success":
        return render(request, 'requestCompleted.html')
    if request.method == 'POST' and request.FILES['myfile']:
        rec = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(rec.name, rec)
        uploaded_file_url = fs.url(filename)
        return render(request, 'donorupdate.html', {
            'uploaded_file_url': uploaded_file_url
        })
    try:
        if detail.points != 0:
            return render(request, 'updatesucess.html')
        donor_id = detail.donor_id.id

        # # verify logged user is one who received sms
        # if donor_id != request.user.last_name:
        #     return render(request, 'errorPage.html')
        req_id = detail.req_id.id
        donor = DonorList.objects.get(pk=donor_id)
        receipt = RequestedRecord.objects.get(pk=req_id)

        #changing status to donor since donor may have accepted request
        RequestedRecord.objects.filter(pk=req_id).update(status="donor")
        context = {
            'donor' : donor, 
            'receipt' : receipt
        }
        return render(request, 'donorupdate.html', context)
    except BaseException as e:
        print(e)
        return render(request, 'errorPage.html')

def updatepoints(request):
    if request.method == 'POST':
        d = request.POST
        msg = ""
        bClass = 'text-danger'
        try:
            pointsObj = Points.objects.filter(pk=d['pid'])
            Points.objects.filter(pk=d['pid']).update(points=int(d['ppoints']))
            msg = "Points Updated"
            bClass = 'text-success'
        except: msg="Given points id not found"
        return render(request,"updatepoints.html",{'check':True,'msg':msg,'bClass':bClass})
    return render(request,"updatepoints.html")

@login_required 
def showpoints(request):
    try:
        donorIns = DonorList.objects.get(pk=request.user.last_name)
        print(request.user.last_name)
        upoints = Points.objects.filter(donor_id = donorIns)
        totalPoints = 0
        for upoint in upoints:
            totalPoints+=int(upoint.points)
        details = {
            'name': donorIns.name,
            'points':totalPoints
        }
        print(details)
        return render(request,"displayPoints.html",{'details':details})
    except BaseException as e:
        print(e)
        return render(request,"errorPage.html")

