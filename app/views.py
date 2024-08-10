from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']

            TO=Topic.objects.get(topicname=tn)
            WO=Webpage.objects.get_or_create(topicname=TO,name=na,url=url)[0]
            WO.save()
            return HttpResponse('webpage is created')
        else:
            return HttpResponse('invalid data')
        
    return render(request,'insert_webpage.html',d)
