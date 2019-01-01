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


@login_required
@csrf_exempt
def uploadFotoDonasi(request):
    fs = FileSystemStorage()
    if (FotoDonasi.objects.count() > 0):
        foto = FotoDonasi.objects.all()
        fs.delete(foto[0].namaFile)
        FotoDonasi.objects.all().delete()
        print("hapus gambar")

        if request.method == 'POST' and request.FILES['fotoDonasi']:
            myfile = request.FILES['fotoDonasi']
            # print(myfile,type(myfile))
            # print(myfile.name, type(myfile.name))
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            urlFotoDonasi = FotoDonasi(
                namaFile=myfile.name,
                urlFoto=uploaded_file_url)
            urlFotoDonasi.save()
            print("simpan foto donasi")
    else:
        if request.method == 'POST' and request.FILES['fotoDonasi']:
            myfile = request.FILES['fotoDonasi']
            # print(myfile, type(myfile))
            # print(myfile.name, type(myfile.name))
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            urlFotoDonasi = FotoDonasi(
                namaFile=myfile.name,
                urlFoto=uploaded_file_url)
            urlFotoDonasi.save()
            print("simpan foto donasi")
    return redirect('wakafadmin:pageFotoDonasi')


@login_required
def pageFotoDonasi(request):
    fotoDonasi = FotoDonasi.objects.all()
    response['fotoDonasi'] = fotoDonasi
    return render(request, 'fotoDonasi.html', response)


@login_required
def pageCarouselHome(request):
    fotoCarousel = CarouselPortofolio.objects.all()
    response['fotoCarousel'] = fotoCarousel
    return render(request, 'fotoCarousel.html', response)


@login_required
@csrf_exempt
def addCarouselHome(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['fotoCarouselHome']:
        myfile = request.FILES['fotoCarouselHome']
        # print(myfile,type(myfile))
        # print(myfile.name, type(myfile.name))
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        urlFotoCarousel = CarouselPortofolio(
            namaFile=myfile.name,
            urlFoto=uploaded_file_url)
        urlFotoCarousel.save()
        print("simpan foto carousel")
    return redirect('wakafadmin:pageCarouselHome')


def deleteCarouselHome(request, image_id):
    fs = FileSystemStorage()
    foto = CarouselPortofolio.objects.get(pk=image_id)
    fs.delete(foto.namaFile)
    foto.delete()
    print("hapus gambar")
    return redirect('wakafadmin:tables')
