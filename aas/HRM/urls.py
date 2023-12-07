from django.urls import path
from . import views


urlpatterns = [
    # login and desboard urls paths

    path('', views.index, name='assindeex' ),
    path('hrlogin', views.hrlogin, name='login' ),
    path('profile/<str:id>', views.profile, name='profile' ),
    
    # add emp urls paths
    path('addemp', views.openempaddpage, name='openempaddpage' ),
    # path('addempstatus', views.addemp, name='addsemstatus' ),

    #add emp leave urls paths
    path('showleaverequest', views.showleaverequest, name='showleave' ),
    path('leavestatus/<str:id>', views.leavestatus, name='leavestatus' ),

    # attenance urls paths

    path('absentworker', views.absentworker, name='absentworker' ),
    path('manualattendace/<str:id>', views.manualattendace, name='manualattendance' ),
    
    path('presentemplyees', views.presentemployees, name='presentemployees' ),
    
]