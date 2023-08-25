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






def Insert_Display_Topic(request):

    tn=input('entern topic_name:')
    to=Topic.objects.create(Topic_name=tn)
    to.save()

    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'Display_Topic.html',d)
    
    

def Insert_Display_Webpage(request):

    tn=input('enter topic_name')
    to=Topic.objects.get(Topic_name=tn)#get method is used to get the object(already available object must give)
    
    name=input('enter name:')
    url=input('enter url:')
    wo=Webpage.objects.get_or_create(Topic_name=to,name=name,url=url)[0]
    wo.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'Display_Webpage.html',d)



def Insert_Display_AccessRecords(request):
    pk=int(input('enter pk'))

    wo=Webpage.objects.get(pk=pk)

    date=input('enter date:')
    author=input('enter autor:')
    email=input('enter email:')

    ao=AccessRecords.objects.get_or_create(name=wo,date=date,author=author,email=email)[0]
    ao.save()

    QSARO=AccessRecords.objects.all()
    d={'QSARO':QSARO}
    return render(request,'Display_AccessRecords.html',d)


    

    
