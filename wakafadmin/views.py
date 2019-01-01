import io
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wakafapp.models import *

response = {}


def show_login(request):
    return render(request, 'login.html', response)

@login_required
def tables(request):
    donaturList = Donatur.objects.all()
    response['donaturList'] = donaturList
    return render(request, 'dashboard.html', response)
