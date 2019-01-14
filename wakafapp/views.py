from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
response = {}
def home(request):
    layanan = Layanan.objects.all()
    response['listLayanan'] = layanan
    fotoDonasi = FotoDonasi.objects.all()
    response['fotoDonasi'] = fotoDonasi
    fotoCarousel = CarouselPortofolio.objects.all()
    response['fotoCarousel'] = fotoCarousel
    testi1 = Testimoni1.objects.all()
    testi2 = Testimoni2.objects.all()
    testi3 = Testimoni3.objects.all()
    response['testi1'] = testi1
    response['testi2'] = testi2
    response['testi3'] = testi3
    response['cmsDonasi'] = DonasiCMS.objects.all()

    return render(request, 'home.html', response)


def program(request):
    response['listProgram'] = UnitBisnis.objects.all()
    return render(request, "program.html", response)

def aboutUs(request):
    return render(request, "aboutUs.html")

def volunteer(request):
    listKegiatanVolunteer = KegiatanVolunteer.objects.all()
    response['listKegiatanVolunteer'] = listKegiatanVolunteer
    page = request.GET.get('page', 1)
    paginator = Paginator(listKegiatanVolunteer, 3)
    try:
        volunteers = paginator.page(page)
    except PageNotAnInteger:
        volunteers = paginator.page(1)
    except EmptyPage:
        volunteers = paginator.page(paginator.num_pages)
    response['listKegiatanVolunteer'] = volunteers

    # Get the index of the current page
    index = volunteers.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    print(page_range)
    response['page_range'] = page_range
    return render(request, "volunteer.html",response)

def artikel(request):
    listArtikel = Artikel.objects.all()
    response['listArtikelRekomendasi'] = ArtikelRekomendasi.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(listArtikel, 3)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    response['listArtikel'] = articles

    # Get the index of the current page
    index = articles.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    print(page_range)
    response['page_range'] = page_range
    return render(request, "artikel.html", response)


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

@csrf_exempt
def add_relawan(request):
    print('masuk add volu')
    if (request.method == 'POST'):
        kegiatan = request.POST['kegiatan']
        namadepan = request.POST['namadepan']
        namabelakang = request.POST['namabelakang']
        email = request.POST['email']
        noHp = request.POST['nohandphone']
        kelamin = request.POST['kelamin']
        alamat = request.POST['alamat']
        birth = request.POST['birthdate']
        domisili = request.POST['domisili']

        volunteer = Volunteer(
            kegiatan=kegiatan,
            nama=namadepan+' '+namabelakang,
            email=email,
            noHp=noHp,
            kelamin=kelamin,
            alamat=alamat,
            birth=birth,
            domisili=domisili
        )
        volunteer.save()
        print('masuk saved')
        print(Volunteer.objects.all().count())
        # TODO: Redirect ke page Thank you
    return HttpResponseRedirect(reverse('wakafapp:volunteer'))

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
