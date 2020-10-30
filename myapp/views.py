from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *


def home(request):
    trainers=trainer.objects.all()
    courses=course.objects.all()
    scount=student.objects.all().count()
    tcount=trainer.objects.all().count()
    count=course.objects.all().count()
    return render(request, 'index.html', {'trn':trainers, 'core':courses, 'scounts':scount, 'tcounts':tcount, 'counts':count })


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def courses(request):
    courses=course.objects.all()
    return render(request,"courses.html", {'core':courses}) 

def trainers(request):
    trainers=trainer.objects.all()
    return render(request,"trainers.html", {'trn':trainers})    