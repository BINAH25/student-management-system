from django import forms
from student.models import *


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staffs
        fields = ['address']

