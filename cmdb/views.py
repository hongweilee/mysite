# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import Form
from django.shortcuts import render
from django.shortcuts import HttpResponse

# #Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(reguest):

    idss=reguest.GET.get("idss",None)
    name=reguest.GET.get("name",None)
    # aa=str(idss)+str(name)

    return  render(reguest,"index.html")

def ind(request):

    if request.method=='POST':
        print request.POST
        username=request.POST['username']
        password=request.POST['password']
        print username,password
    return  render(request,"index.html")
