from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date, datetime
# from HRM.models import Employee, Leave
from .models import Employee, Leave, Attendance, LeaveCount

import random
# from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# f = Fernet(key)
# Create your views here.


def index(request):
    return render(request, 'worker/home.html')

def home(request):
    return render(request, 'worker/home.html')

def profile(request, id ):
    data = Employee.objects.get(emp_id = id)
    param = {
        'data': data
    }

    return render(request, 'worker/profile.html', param)

def openpasschange(request):
    return render(request, 'worker/change.html')
def passchange(request):

    var_empid = request.POST.get('username')
    var_email = request.POST.get('email')
    var_pass = request.POST.get('password')
    var_cpass = request.POST.get('cpassword')
    print(var_empid)
  
    if request.method == 'POST':
        # try:
            emp = Employee.objects.get(emp_id = var_empid)
            database_email =emp.emp_email
            if  database_email == var_email:

                if var_pass == var_cpass:
                    # plainText = var_pass.encode()
                    # encryptedpassword = f.encrypt(plainText)

                    emp.emp_pass = var_pass
                    emp.save()
                    return redirect('/worker')
                else:
                    return HttpResponse("please enter same password")
            else:
            
                return HttpResponse("data is not match")
        # except:
            return HttpResponse("please enter correct username")


def workerlogin(request):
    if request.method == 'POST':
        
        # try:
            
            username =  request.POST.get('username',)
            password = request.POST.get('password')
            var_emp_id = Employee.objects.filter(emp_id = username).count()
            if int(var_emp_id) == 1:
                
                val_emp = Employee.objects.get(emp_id = username)

                param ={ 'guserid' : val_emp }
                var_attendance =  Attendance.objects.get(emp_id = username)
                var_attendance_date = var_attendance.attendace_date
                var_attendance_time = var_attendance.attendance_time

                if var_attendance_date == date.today():
                    param['time'] = var_attendance_time
                    param['cls'] = "text-green-500"
                else:
                    param['time'] = 'Absent'
                    param['cls'] = 'text-red-900'

# Session start
                request.session['userid'] = username
                var_emp_pass = val_emp.emp_pass
                if var_emp_pass == password:
                   return render(request, 'worker/workerdeshboard.html',param)
                else:
                    return HttpResponse("<h1>Please Enter the right password")

        # except:
        #     return render(request, 'HRM/error.html')
    return HttpResponse("post if error")

    # return render(request, 'HRM/error2.html')

def leaveapplication(request):

    # Employee basic info fetch from Employee table
    id = request.session['userid']
    data =  Employee.objects.get(emp_id = id)
    data2 =  LeaveCount.objects.get(emp_id = id)

    param ={'empdata':data,
            'leavedata': data2

            }
    return render(request, 'worker/applyleave.html', param)

def applyleave(request):

    var_emp_id =  request.POST.get('empid')
    var_emp_name =  request.POST.get('empname')
    var_emp_dep =  request.POST.get('empdep')
    var_s_date =  request.POST.get('leavestart')
    var_e_date =  request.POST.get('leaveend')
    var_l_type =  request.POST.get('leavetype')
    var_random_leave_id = random.randint(10000, 99999)
    if request.method == 'POST':
        data = Employee.objects.get(emp_id = var_emp_id)
        data2 = Attendance.objects.get(emp_id = var_emp_id)
        data3 = data2.attendance_time
        
        d1 = datetime.strptime(var_s_date,"%Y-%m-%d").date()
        d2 = datetime.strptime(var_e_date,"%Y-%m-%d").date()


        var_l_day = str(int((d2- d1).days) +1)
        quary =  Leave(leave_id = var_random_leave_id, emp_id = var_emp_id, emp_name = var_emp_name, emp_dep = var_emp_dep, s_date = var_s_date, e_date = var_e_date, l_day = var_l_day, l_type = var_l_type, l_status = "Pending")
        quary.save()

        if var_l_type == 'medical':
            quary2 =  LeaveCount.objects.get(emp_id = var_emp_id)
            # print(quary2)
            var_medical = quary2.medical_leave
            # print(var_medical)
            remaining_medical = var_medical -int(var_l_day)
            # print(remaining_medical)

            quary2.medical_leave = remaining_medical
            # print(var_medical)
            quary2.save()
            quary.save()
        if var_l_type == 'personal':
            quary2 =  LeaveCount.objects.get(emp_id = var_emp_id)
            var_personal = quary2.personal_leave
            # print(var_personal)
            remaining_personal = var_personal - int(var_l_day)
            # print(remaining_personal)
            quary2.personal_leave = remaining_personal
            quary2.save()
            quary.save()
        param = {"leavemessage" : "leave request send successfully"}

        param['day'] = var_l_day
        param['guserid'] = data
        param['time'] = data3
        return render(request, 'worker/workerdeshboard.html', param)
    else:
        return HttpResponse("failed")

    # return HttpResponse("testing")

def appliedleavestatus(request):

    id = request.session['userid']
    data =  Leave.objects.filter(emp_id = id).order_by('s_date')
    # photo =  Employee.objects.get(emp_id =  id)

    param =  {'leavestatus': data}

    # return HttpResponse(id)
    return render(request, 'worker/leavestatus.html', param)