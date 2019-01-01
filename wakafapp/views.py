from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


# Create your views here.
response = {}
def home(request):
    fotoDonasi = FotoDonasi.objects.all()
    response['fotoDonasi'] = fotoDonasi
    fotoCarousel = CarouselPortofolio.objects.all()
    response['fotoCarousel'] = fotoCarousel
    return render(request, 'home.html', response)


def program(request):
    return render(request, "program.html")


def volunteer(request):
    return render(request, "volunteer.html")


def article(request):
    return render(request, "article.html")


@csrf_exempt
def add_donatur(request):
    if (request.method == 'POST'):
        nominal = request.POST['nominal']
        namadepan = request.POST['namadepan']
        namabelakang = request.POST['namabelakang']
        email = request.POST['email']
        noHp = request.POST['nohandphone']
        kelamin = request.POST['kelamin']
        alamat = request.POST['alamat']
        birth = request.POST['birthdate']
        domisili = request.POST['domisili']

        donatur = Donatur(
            nominal=nominal,
            nama=namadepan+' '+namabelakang,
            email=email,
            noHp=noHp,
            kelamin=kelamin,
            alamat=alamat,
            birth=birth,
            domisili=domisili
        )
        donatur.save()
        print(Donatur.objects.all().count())
        # TODO: Redirect ke page Thank you
    return HttpResponseRedirect(reverse('wakafapp:home'))


def coba(request):
    a = Parent.objects.all().delete()
    b = Child.objects.all().delete()
    print(Parent.objects.all().count())
    print(Child.objects.all().count())
    response = {}
    parent1 = Parent(nama="azhar")
    parent1.save()
    child = Child(parent= Parent.objects.get(nama="azhar"), value='a')
    child.save()
    child = Child(parent=Parent.objects.get(nama="azhar"), value='aaa')
    child.save()
    response['parent'] = Parent.objects.all()
    response['child'] = Child.objects.all()
    return render(request, "coba.html", response)

# def testtt(request):
# 	return render(request,'home-old.html')
