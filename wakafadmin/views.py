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

@login_required
def deleteCarouselHome(request, image_id):
    fs = FileSystemStorage()
    foto = CarouselPortofolio.objects.get(pk=image_id)
    fs.delete(foto.namaFile)
    foto.delete()
    print("hapus gambar")
    return redirect('wakafadmin:tables')

@login_required
@csrf_exempt
def addLayanan(request):
    if request.method == 'POST':
        judul = request.POST['judul']
        konten = request.POST['konten']
        layanan = Layanan(
            judul=judul,
            konten=konten
        )
        layanan.save()
    return redirect('wakafadmin:pageLayanan')
@login_required
def pageLayanan(request):
    listLayanan = Layanan.objects.all()
    response['listLayanan'] = listLayanan
    return render(request, 'layanan.html', response)

@login_required
def deleteLayanan(request, layanan_id):
    layanan = Layanan.objects.get(pk=layanan_id)
    layanan.delete()
    return redirect('wakafadmin:pageLayanan')

@login_required
def pageEditTesti(request):
    testi1 = Testimoni1.objects.all()
    testi2 = Testimoni2.objects.all()
    testi3 = Testimoni3.objects.all()
    response = {'testi1':testi1, 'testi2':testi2, 'testi3':testi3}
    return render(request, 'testi.html',response)

@login_required
@csrf_exempt
def addTesti(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['fotoTesti']:

        if request.POST['letak'] == '1':
            if Testimoni1.objects.count() > 0:
                testi = Testimoni1.objects.all()
                fs.delete(testi[0].namaFile)
                testi.delete()

                myfile = request.FILES['fotoTesti']
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("simpan foto donasi")
                testi = Testimoni1(
                    namaFile=myfile.name,
                    urlFoto=uploaded_file_url,
                    konten=request.POST['konten'],
                    nama=request.POST['nama'],
                    jabatan=request.POST['jabatan']
                )
                testi.save()
            else:
                myfile = request.FILES['fotoTesti']
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("simpan foto donasi")
                testi = Testimoni1(
                    namaFile=myfile.name,
                    urlFoto=uploaded_file_url,
                    konten=request.POST['konten'],
                    nama=request.POST['nama'],
                    jabatan=request.POST['jabatan']
                )
                testi.save()


        elif request.POST['letak'] == '2':
            if Testimoni2.objects.count() > 0:
                testi = Testimoni2.objects.all()
                fs.delete(testi[0].namaFile)
                testi.delete()

                myfile = request.FILES['fotoTesti']
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("simpan foto donasi")
                testi = Testimoni1(
                    namaFile=myfile.name,
                    urlFoto=uploaded_file_url,
                    konten=request.POST['konten'],
                    nama=request.POST['nama'],
                    jabatan=request.POST['jabatan']
                )
                testi.save()
            else:
                myfile = request.FILES['fotoTesti']
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("simpan foto donasi")
                testi = Testimoni2(
                    namaFile=myfile.name,
                    urlFoto=uploaded_file_url,
                    konten=request.POST['konten'],
                    nama=request.POST['nama'],
                    jabatan=request.POST['jabatan']
                )
                testi.save()
        elif request.POST['letak'] == '3':
            if Testimoni3.objects.count() > 0:
                testi = Testimoni1.objects.all()
                fs.delete(testi[0].namaFile)
                testi.delete()

                myfile = request.FILES['fotoTesti']
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("simpan foto donasi")
                testi = Testimoni3(
                    namaFile=myfile.name,
                    urlFoto=uploaded_file_url,
                    konten=request.POST['konten'],
                    nama=request.POST['nama'],
                    jabatan=request.POST['jabatan']
                )
                testi.save()
            else:
                myfile = request.FILES['fotoTesti']
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print("simpan foto donasi")
                testi = Testimoni3(
                    namaFile=myfile.name,
                    urlFoto=uploaded_file_url,
                    konten=request.POST['konten'],
                    nama=request.POST['nama'],
                    jabatan=request.POST['jabatan']
                )
                testi.save()

    return redirect('wakafadmin:pageEditTesti')

@login_required
def deleteTesti1(request, testi_id):
    fs = FileSystemStorage()
    testi = Testimoni1.objects.get(pk=testi_id)
    fs.delete(testi.namaFile)
    testi.delete()
    return redirect('wakafadmin:pageEditTesti')

@login_required
def deleteTesti2(request, testi_id):
    fs = FileSystemStorage()
    testi = Testimoni2.objects.get(pk=testi_id)
    fs.delete(testi.namaFile)
    testi.delete()
    return redirect('wakafadmin:pageEditTesti')

@login_required
def deleteTesti3(request, testi_id):
    fs = FileSystemStorage()
    testi = Testimoni3.objects.get(pk=testi_id)
    fs.delete(testi.namaFile)
    testi.delete()
    return redirect('wakafadmin:pageEditTesti')

@login_required
def pageProgram(request):
    response['listProgram'] = UnitBisnis.objects.all()
    return render(request,'pageEditProgram.html',response)

@login_required
@csrf_exempt
def addProgram(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['fotoProgram']:
        myfile = request.FILES['fotoProgram']
        judul = request.POST['nama']
        konten = request.POST['konten']
        indikator = request.POST['indikator']
        # print(myfile.name, type(myfile.name))
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        urlFotoProgram = UnitBisnis(
            namaFile=myfile.name,
            urlFoto=uploaded_file_url,
            judul=judul,
            konten=konten,
            indikator=indikator
        )
        urlFotoProgram.save()
        print("simpan program")
    return redirect('wakafadmin:pageProgram')

@login_required
def deleteProgram(request, program_id):
    fs = FileSystemStorage()
    program = UnitBisnis.objects.get(pk=program_id)
    fs.delete(program.namaFile)
    program.delete()
    return redirect('wakafadmin:pageProgram')

