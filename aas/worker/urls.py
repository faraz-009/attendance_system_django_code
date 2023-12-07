from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='workerindex' ),
    #login urls paths
    path('workerlogin', views.workerlogin, name='workerlogin' ),
    path('profile/<str:id>', views.profile, name='profile' ),

    #leave urls paths

    path('leaveapplication', views.leaveapplication, name='leaveapplication' ),
    path('applyleave', views.applyleave, name='applyleave' ),
    path('appliedleavestatus', views.appliedleavestatus, name='appliedleavestatus' ),

    # change password

    path('openpasschange', views.openpasschange, name='passwordform' ),
    path('passchange', views.passchange, name='passwordchange' ),

    
    # 
    
]