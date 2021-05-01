from twilio.rest import Client #pip install twilio
from random import randint
class Notify:
    def __init__(self,accountID,authToken,from_ = None):
        self.__accountID = accountID
        self.__authToken = authToken
        self.__client = Client(self.__accountID,self.__authToken)
        self.__from = from_
        if from_ == None:
            self.__from = '+18625052631'
        self.__status = None
    
    def send_sms(self,to,body):
        try:
            self.__status = self.__client.messages.create(body=body, from_ = self.__from, to=to)
        except Exception as e:
            print("Failed to send sms to",to,"error:",e)

    def __generateOTP(self,otpLength):
        otp = ""
        for c in range(otpLength):
            otp+=str(randint(0,9))
        return otp
    
    def send_otp(self,to,otpLength = 6):
        otp = self.__generateOTP(otpLength)
        body = "Enter "+ otp + " to verify your number"
        self.send_sms(to,body)
        return '-1' if self.__status is None else otp

