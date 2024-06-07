from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from datetime import date, datetime
from .models import Hradmin, Employee,Leave, Attendance
from .form import EmployeeForm, AttendanceForm, LeaveAndAttendanceCountForm


# Create your views here.

def index(request):
    return render(request, 'HRM/home.html')

def profile(request, id ):
    data = Employee.objects.get(emp_id = i)
    param = {
        'data': data
    }

    return render(request, 'HRM/profile.html', param)

def hrlogin(request):

    if request.method == 'POST':
        
        # try:
            
            username =  request.POST.get('username')
            password = request.POST.get('password')
            var_emp_id = Hradmin.objects.filter(emp_id = username).count()
            if int(var_emp_id) == 1:
                request
                val_emp_id = Hradmin.objects.get(emp_id = username)
                var_emp_pass = val_emp_id.emp_pass

                param ={ 'userid' : val_emp_id }

                if var_emp_pass == password:
                    return render(request, 'HRM/hrdeshboard.html', param)
                else:
                    return HttpResponse("<h1>Please Enter the right password</h>")

        # except:
        #     return render(request, 'HRM/error.html')

    return render(request, 'HRM/error2.html')

def openempaddpage(request):
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        form2 = AttendanceForm(request.POST)
        form3 = LeaveAndAttendanceCountForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
    
    form = EmployeeForm()
    return render(request,"HRM/addemployee.html",{'form': form}) 
    
def showleaverequest(request):

    var_status_list = ["Accept","Reject"]
    var_all_leave =  Leave.objects.exclude(l_status__in = var_status_list).order_by('s_date')
    
    param =  {'allleave': var_all_leave}
    return render(request, 'HRM/checkleaverequest.html', param)


def leavestatus(request, id):
    if request.method == 'POST':
        var_accpet_status =  request.POST.get("accept")
        var_reject_status =  request.POST.get("reject")

        if var_accpet_status == 'Accept':
            data =  Leave.objects.get(leave_id = id)
            data.l_status = "Accept"
            data.save()

            # this is a start end of illogical algorithm

            var_status_list = ["Accept","Reject"]
            var_all_leave =  Leave.objects.exclude(l_status__in = var_status_list).order_by('s_date')
    
            param =  {'allleave': var_all_leave,
                        'message' : "Leave request accepted"
                        }
            # illogical algorithm

            return render(request,'HRM/checkleaverequest.html', param)

            # return HttpResponse("kya h yrrr")

        elif var_reject_status == 'Reject':
            data =  Leave.objects.get(leave_id =id)
            data.l_status = "Reject"
            data.save()
            param = {'message' :  "Leave request rejected"}


            # this is a start end of illogical algorithm

            var_status_list = ["Accept","Reject"]
            var_all_leave =  Leave.objects.exclude(l_status__in = var_status_list)
            param =  {'allleave': var_all_leave,
                        'message' : "Leave request Rejected"
                        }
            # illogical algorithm

            return render(request,'HRM/checkleaverequest.html', param)
    
    return render(request, "HRM/error.html")
        
def absentworker(request):
    # a = 1000
    # p
    var_all_emp_id = Attendance.objects.exclude(attendace_date = date.today())

    param = {
        'absent': var_all_emp_id
    }

    # pass

    return render(request, 'HRM/adminattendance.html', param)


def manualattendace(request, id):

    var_button = request.POST.get("presnet")

    if request.method == 'POST':
        data =  Attendance.objects.get(emp_id = id)
        var_attendance_count = data.attendance_count
        update_attendanec_count = var_attendance_count +1
        data.attendace_date = date.today()
        data.attendance_time = datetime.now()
        
        data.attendance_count =  update_attendanec_count
        data.save()

        var_all_emp_id = Attendance.objects.exclude(attendace_date = date.today())

        param = {
        'absent': var_all_emp_id
        }

        return render(request, 'HRM/adminattendance.html', param)
    return HttpResponse("Kuch galt ho raha hai.... keep it upp!!!")

def presentemployees(request):
    var_pre_emp = Attendance.objects.filter(attendace_date = date.today())
    # var_info =Employee.objects.filter(emp_id = Attendance.objects.filter(attendace_date = date.today()))

    param = {
        'persent' :  var_pre_emp,
        # 'info': var_info
    }

    return render(request, 'HRM/presentemployees.html', param)
