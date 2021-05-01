from django.urls import path
from .views import searchdisplay, donorlistdetail, donorupdate, updatepoints, showpoints

urlpatterns = [
    path('', searchdisplay, name='searchsite1'),
    path('donorlist/', searchdisplay, name='donorlistsite'),
    path('donorlist/donorlistdetail/<email>/', donorlistdetail, name='donorlistdetailsite'),
    path('donorupdate/<cid>/', donorupdate, name='donorupdatesite'),
    path('updatepoints/', updatepoints, name='updateuserpoints'),
    path('points/', showpoints, name='userpoints'),
]