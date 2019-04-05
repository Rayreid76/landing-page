# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, "resume/index.html")

def sent(request):
    name = request.POST["name"]
    email = request.POST["email"]
    text = request.POST["text"]
    errors =  Texts.object.textValidation(name, email,text)
    if len(errors) == 0:
        return redirect("/")
    else:
        for message in errors:
            messages.error(request, message)
        return redirect("/")