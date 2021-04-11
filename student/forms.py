from django import forms
from .models import Student
from django.forms import ModelForm

class StuForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

