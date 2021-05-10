import os
import threading
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
from django.http import request
from dreg .models import DonorList
from .models import Points
from .models import RequestedRecord
from .np import Notify

aid = os.getenv('aid')
aToken = os.getenv('aToken')
twilioNumber = os.getenv('twilioNumber')
domain = os.getenv('domain')
domain = domain + 'search/donorupdate/'
send_sms = True
maximum_sms = 2
distanceConstant = 20 #radius of area to cover in KM

def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)


#return list of donors who has given bloodgroup
# and is under certain area and outside of certain area
def findEligibleDonors(blood_group,minimumDistance,maximumDistance,lat1,lon1):
    eligibleDonors = list()
    for donor in DonorList.objects.filter(blood_group__iexact = blood_group):
        if donor.location:
            lat,lon = map(float,donor.location)
            donorReceiptDistance = distance(lat1,lat,lon1,lon)
            # print(donor.address,donor.location,donorReceiptDistance)
            if donorReceiptDistance >= minimumDistance and donorReceiptDistance < maximumDistance:
                eligibleDonors.append(donor)
    return eligibleDonors

def sendSMSToEligibleDonors(eligibleDonors,requestRec):
    print(eligibleDonors)
    notifyObj = Notify(aid,aToken,twilioNumber)
    units = requestRec.units
    blood_group = requestRec.blood_group
    contact_number = requestRec.contact_number
    for ind in range(min(units,len(eligibleDonors),maximum_sms)):
        donor = eligibleDonors[ind]
        pointsID = Points.objects.create(donor_id=donor,req_id=requestRec,points=0)
        msg = "Someone needs "+blood_group+" blood. Please contact "+str(contact_number)+ " after donation Kindly update info on "+domain+str(pointsID.id)
        dPh = str(donor.phone_number)
        if dPh[0]!="+":
            dPh = "+91"+dPh
        if send_sms:
            notifyObj.send_sms(dPh,msg)
        else:
            print("[SMS Disabled]","to",dPh,"body",msg)


def increaseArea():
    print("checking for pending requests")
    #find all pending request
    reqs = RequestedRecord.objects.filter(status__iexact = 'pending')

    currentTime = datetime.now()
    for req in reqs:
        diff = (req.created_at - currentTime).total_seconds() // 60 #elapsed time in minutes
        lat,lon = map(float,req.location)
        areaToCoverRadius = distanceConstant
        previousArea = 0
        if diff > 10 and diff <= 30:
            previousArea = distanceConstant
            areaToCoverRadius*=2
        elif diff > 30 and diff <= 120:
            previousArea = distanceConstant*2
            areaToCoverRadius*=4
        else:
            previousArea = float("inf")
            areaToCoverRadius = float("inf")
        eligibleDonors = findEligibleDonors(req.blood_group,previousArea,areaToCoverRadius,lat,lon)
        sendSMSToEligibleDonors(eligibleDonors,req)

def notify_donor(receipt,forms):
    blood_group = receipt["blood_group"]
    city = receipt["location"]
    units = receipt["units"]
    addr = receipt["address"]
    contact_number = receipt["contact_number"]
    donors = DonorList.objects.filter(
        blood_group__iexact = blood_group)
    if donors.count() == 0:
        print("No donor found")
    else:
        if city:
            lat1,lon1 = map(float, city.split(","))
        
        # changing status to pending before submitting
        forms.save(commit=False)
        forms.status = 'pending'
        requestRec = forms.save()

        # donor who lies in on area of receipt
        eligibleDonors = findEligibleDonors(blood_group,0,distanceConstant,lat1,lon1)
        sendSMSToEligibleDonors(eligibleDonors,requestRec)