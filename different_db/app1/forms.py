from django import forms
from .models import Student12
class Student_Form(forms.ModelForm):
    class Meta:
        model=Student12
        fields=['idno','name','sal']