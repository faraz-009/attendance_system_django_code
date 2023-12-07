from django.shortcuts import render, redirect
from HRM.models import Hradmin


def index(request):
    return render(request,'index.html')
def home(request):

    if skey in request.sessions.key():
        del request.session[skey]
    return redirect('/')

def about(request):
    return render(request,'about.html')

def contact(request):
    alldata = Hradmin.objects.all()


    param = {
        'data':  alldata
    }
    print(param)
    return render(request, 'contact.html', param)





