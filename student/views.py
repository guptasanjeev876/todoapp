from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import *
# Create your views here.
def home(request):
    task = Student.objects.all()
    form = StuForms()
    if request.method == 'POST':
        form = StuForms(request.POST)
        if form.is_valid:
            form.save()
        form = StuForms
    else:
        form = StuForms()
    tk = Student.objects.all()
    context ={'tk':tk, 'task': task, 'form': form}
    return render(request, 'student/home.html',context) 

def updateTask(request,pk):
    task =  Student.objects.get(id=pk)
    form = StuForms(instance = task)
    if request.method == 'POST':
        form =StuForms(request.POST, instance = task)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request, 'student/update.html', context)

def delete(request,pk):
    item = Student.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
    context ={'item':item}
    return render(request,'student/delete.html', context)