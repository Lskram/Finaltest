from django.shortcuts import render,HttpResponse
from . import models
# Create your views here.

def Home(request):
    context = {}
    classes = models.Classes.objects.all().order_by("name")
   
    context ['classes'] = classes
    return render (request,"home.html", context)
    
def General(request):
    context = {}
    classes = models.Classes.objects.filter(department=1).order_by("name")
   
    context ['classes'] = classes
    return render (request,"general.html", context)
    
def Elective_subjects(request):
    context = {}
    classes = models.Classes.objects.filter(department=2).order_by("name")
   
    context ['classes'] = classes
    return render (request,"elective_subjects.html", context)

def Special_subjects(request):
    context = {}
    classes = models.Classes.objects.filter(department=3).order_by("name")
   
    context ['classes'] = classes
    return render (request,"special_subjects.html", context)

    
def About(request):
    return render (request,"about.html")

def Contact(request):
    return render (request,"contact.html")