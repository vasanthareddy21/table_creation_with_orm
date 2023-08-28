from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def Display_AccessRecords(request):

    #order_by
    QSARO=AccessRecords.objects.all()
    QSARO=AccessRecords.objects.all().order_by('name')

    #year lookup
    QSARO=AccessRecords.objects.filter(date__year='1999')

    #month lookup
    QSARO=AccessRecords.objects.filter(date__month='11')

    #date lookup
    QSARO=AccessRecords.objects.filter(date__day='11')

    #regex lookup
    QSARO=AccessRecords.objects.filter(author__regex='^s\w+')

    #multiple lookups in single coloumn
    QSARO=AccessRecords.objects.filter(date__year__lte='1999')

    QSARO=AccessRecords.objects.filter(date__year__gte='1999')


    d={'QSARO':QSARO}
    return render(request,'Display_AccessRecords.html',d)



def Display_Webpage(request):
    
    QSWO=Webpage.objects.all()
    #order_by
    QSWO=Webpage.objects.all().order_by('Topic_name')#Ascending order
    QSWO=Webpage.objects.all().order_by('-Topic_name')#Descending order
    
    #Based on length
    QSWO=Webpage.objects.all().order_by(Length('name'))#Acending order
    QSWO=Webpage.objects.all().order_by(Length('name').desc()) #Descending order

    #To fetch the any number of rows you want using positive indexing in slicing(we can not use negative indexing)
    QSWO=Webpage.objects.all()[:2]
    QSWO=Webpage.objects.all()[2:5]

    #We use exclude method opposite to the filter method[except cricket anything it will fetch]
    QSWO=Webpage.objects.exclude(Topic_name='cricket')

    #we use filter metod[it will fetch only Boxing]
    QSWO=Webpage.objects.exclude(Topic_name='Boxing')
    

    #it deals with field lookups

    #startswith fieldlookup
    QSWO=Webpage.objects.filter(name__startswith='v')
    QSWO=Webpage.objects.filter(name__startswith='s')

    #endswith fieldlookup
    QSWO=Webpage.objects.filter(url__endswith='a')
    QSWO=Webpage.objects.filter(url__endswith='com')
    QSWO=Webpage.objects.filter(url__endswith='in')

    #contains lookup
    QSWO=Webpage.objects.filter(url__contains='r')
    QSWO=Webpage.objects.exclude(url__contains='r')
    QSWO=Webpage.objects.filter(name__contains='r')

    d={'QSWO':QSWO}
    return render(request,'Display_Webpage.html',d)






    

def Display_Topic(request):

    QSTO=Topic.objects.all()
    QSTO=Topic.objects.all().order_by('Topic_name')

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


    

    
