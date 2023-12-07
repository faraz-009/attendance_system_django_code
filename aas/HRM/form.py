from django import forms
from .models import Employee, Attendance, LeaveCount

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model=Employee
        fields=('emp_id','emp_name','emp_address','emp_phone','emp_dep','emp_email','emp_photo')

        widgets = {
            'emp_id' : forms.TextInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name':'empid'}),
            'emp_name' : forms.TextInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name': 'empname'}),
            'emp_address' : forms.TextInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name':'empaddress'}),
            'emp_phone' : forms.TextInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name' : 'empphone'}),
            'emp_dep' : forms.TextInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name': 'empdep'}),
            'emp_email' : forms.TextInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name': 'empemail'}),
            'emp_photo' : forms.FileInput(attrs={'class': 'djangoform my-2 border w-full border-slate-800 px-5 py-1 hover:drop-shadow-2xl rounded', 'id': '', 'name': 'empphoto'}),
           

        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model =  Attendance
        fields = ('emp_id','emp_name')
class LeaveAndAttendanceCountForm(forms.ModelForm):
    class Meta:
        model =  LeaveCount
        fields = ('emp_id',)

