from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAFO=Accessform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=Accessform(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(name=n)
            a=AFDO.cleaned_data['author']
            d=AFDO.cleaned_data['date']
            AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
            AO.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_access.html',d)




