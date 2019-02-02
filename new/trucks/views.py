from django.shortcuts import render, redirect
from django.template import loader
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .tasks import *
from .forms import *
from django.db.models import Q
import datetime
from datetime import date
from .notigenerator import notigene
from .expiry_dates import *


def submit(request):
    if(request.method == 'POST'):
        form = TrucksSubmit(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/submit')
    else:
        form = TrucksSubmit()

    return render(request, 'trucks/homeform.html', {'form': form})


def index(request):
    print(request)
    if(request.method == "POST"):
        obj = Notifications.objects.all()
        for i in obj:
            i.boolean = False
            i.save()
    details = TrucksData.objects.all()
    notigene(details)
    unread = {}
    read = {}
    obj = Notifications.objects.all()
    for i in obj:
        if(i.boolean is True):
            unread[i.data] = i.truck_number
        else:
            read[i.data] = i.truck_number
    # print(noti)
    args = {'details': details, 'read': read, 'unread': unread}
    return render(request, 'trucks/search.html', args)


def information(request, id_no):
    specific_details = TrucksData.objects.filter(truck_number=id_no)
    string = insurance_expiry(specific_details)
    nextstring = fitness_certificate_expiry(specific_details)

    args = {'specific_details': specific_details,
            'string': string, 'nextstring': nextstring}
    return render(request, 'trucks/info.html', args)
