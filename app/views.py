from django.shortcuts import render

# Create your views here.
from app.models import *

def Display_AccessRecords(request):

    QSARO=AccessRecords.objects.all()
    d={'QSARO':QSARO}
    return render(request,'Display_AccessRecords.html',d)

def Display_Webpage(request):
    
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'Display_Webpage.html',d)

def Display_Topic(request):

    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'Display_Topic.html',d)


