from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DonorSearch
from dreg.models import DonorList
from .models import SearchLogo
from .models import Points
from .models import RequestedRecord
from .NotifyDonor import notify_donor
from django.core.files.storage import FileSystemStorage


def searchdisplay(request):
    search_forms = DonorSearch()
    logo_img = SearchLogo.objects.get(logo_number=1)
    if request.method == 'POST':
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            notify_donor(search_forms.cleaned_data)
            return render(request,'reqAccepted.html')
        else:
            return render(request,'errorPage.html')

    context = {
        'forms_search' : search_forms,
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


def donorupdate(request, cid):
    if request.method == 'POST' and request.FILES['myfile']:
        rec = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(rec.name, rec)
        uploaded_file_url = fs.url(filename)
        return render(request, 'donorupdate.html', {
            'uploaded_file_url': uploaded_file_url
        })
    try:
        detail = Points.objects.get(pk=cid)
        if detail.points != 0:
            return render(request, 'updatesucess.html')
        donor_id = detail.donor_id.id
        req_id = detail.req_id.id
        donor = DonorList.objects.get(pk=donor_id)
        receipt = RequestedRecord.objects.get(pk=req_id)
        context = {
            'donor' : donor,
            'receipt' : receipt
        }
        return render(request, 'donorupdate.html', context)
    except BaseException as e:
        print(e)
        return render(request, 'errorPage.html', context)

def updatepoints(request):
    if request.method == 'POST':
        d = request.POST
        pointsObj = Points.objects.filter(pk=d['pid']).update(points=int(d['ppoints']))
        return render(request,"updatepoints.html",{'check':True})
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

