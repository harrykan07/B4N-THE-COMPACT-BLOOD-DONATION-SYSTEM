import os
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

def notify_donor(receipt):
    blood_group = receipt["select_blood_group"]
    city = receipt["city"]
    units = receipt["units"]
    addr = receipt["select_location"]
    contact_number = receipt["mobile_no"]
    donors = DonorList.objects.filter(
        blood_group__iexact = blood_group,
        home_address__icontains = city)
    if donors.count() == 0:
        print("No donor found")
    else:
        requestRec = RequestedRecord.objects.create(units=units,addr=addr,city=city,contact_number=contact_number)
        notifyObj = Notify(aid,aToken,twilioNumber)
        for ind in range(min(units,len(donors),maximum_sms)):
            donor = donors[ind]
            pointsID = Points.objects.create(donor_id=donor,req_id=requestRec,points=0)
            msg = "Someone needs "+blood_group+" blood. Please contact "+str(contact_number)+ " after donation Kindly update info on "+domain+str(pointsID.id)
            dPh = str(donor.phone_number)
            if dPh[0]!="+":
                dPh = "+91"+dPh
            if send_sms:
                notifyObj.send_sms(dPh,msg)
        pass
    pass