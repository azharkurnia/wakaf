from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random, string
from django.core.mail import EmailMessage, send_mail

from django.core.files.storage import FileSystemStorage


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
    try:
        last_id = int(Donatur.objects.last().pk) + 1
    except:
        last_id = 1
    id_transaksi = '#'+''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

    if (request.method == 'POST'):
        nominal = int(request.POST['nominal'])
        namadepan = request.POST['namadepan']
        namabelakang = request.POST['namabelakang']
        emailUser = request.POST['email']
        noHp = request.POST['nohandphone']
        kelamin = request.POST['kelamin']
        alamat = request.POST['alamat']
        birth = request.POST['birthdate']
        domisili = request.POST['domisili']
        nama = namadepan +' '+namabelakang
        id_transaksi = id_transaksi+'00'+str(last_id)
        kode_transfer = int(random.randint(1,100))
        donatur = Donatur(
            nominal=nominal,
            nama=namadepan+' '+namabelakang,
            email=emailUser,
            noHp=noHp,
            kelamin=kelamin,
            alamat=alamat,
            birth=birth,
            domisili=domisili,
            id_transaksi=id_transaksi,
            kode_transfer=kode_transfer,
            jumlah_donasi=int(nominal+kode_transfer)
        )
        donatur.save()
        print(Donatur.objects.all().count())
        pesan = "Assalamu'alaikum Warrahmatullahi Wabarakaatuh \n" \
                + 'Alhamdulillah, kami mengucapkan terima kasih kepada ' + kelamin + ' ' + nama + ' telah melakukan donasi kepada Yayasan Wakaf Produktif – Pengelola Aset Islami Indonesia.\n\n' \
                + 'Berikut adalah rincian donasi ' + kelamin + ' ' + nama + '\n\n' \
                + 'No Transaksi: ' + id_transaksi + '\n' \
                + 'Nama: ' + nama+ '\n' \
                + 'Tanggal Lahir: ' + birth +'\n' \
                + 'Alamat: ' + alamat + '\n' \
                + 'Domisili: ' + domisili + '\n' \
                + 'Jumlah Donasi: Rp ' + str(nominal) +'\n' \
                + 'Kode Unik: ' + str(kode_transfer) +'\n' \
                + 'Nominal Transfer: Rp ' + str(int(nominal+kode_transfer)) + '\n\n' \
                + 'Silahkan melanjutkan pembayaran donasi ke rekening kami:\n' \
                + 'Bank CIMB Niaga Syariah\n' \
                + 'No. Rekening: 761868208100\n' \
                + 'Atas Nama: YAYASAN WAKAF PRODUKTIF PENGELOLA ASET ISLAMI INDONESIA\n\n' \
                + 'Setelah anda melakukan pembayaran, silahkan lakukan konfirmasi di http://wakaf.paii.co.id/konfirmasi\n\n' \
                + 'Untuk informasi lebih lanjut, anda dapat menghubungi:\n' \
                + 'Call Center: 021-123456\n' \
                + 'SMS/WA: 0812-9060-9550\n' \
                + 'Email: info@wakaf.paii.co.id\n' \
                + 'Website: wakaf.paii.co.id\n\n'\
                + "“Jazakumullah khairan katsiran. Wa jazakumullah ahsanal jaza”\n" \
                + 'Yayasan Wakaf Produktif – Pengelola Aset Islami Indonesia'
        email = EmailMessage(
            'Informasi dan Langkah Donasi',
            pesan,
            'info@wakaf.paii.co.di',
            [emailUser],
            headers={'Message-ID': 'foo'}
        )
        email.send(fail_silently=False)
        print("email sent")
        # TODO: Redirect ke page Thank you

        return thankyouDonasi(request, donatur)
    return HttpResponseRedirect(reverse('wakafapp:home'))

def thankyouDonasi(request, data=None):
    if data:
        data = data.__dict__
        return render(request, "thankyouDonasi.html", data)

    else:
        return home(request)

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
        return thankyouVolunteer(request, volunteer)


def thankyouVolunteer(request, data=None):
    if data:
        data = data.__dict__
        return render(request, "thankyouVolunteer.html", data)

    else:
        return volunteer(request)

def konfirmasi(request):
    return render(request, "konfirmasi.html")

def thankyouKonfirmasi(request):
    return render(request, 'thankyouKonfirmasi.html')

@csrf_exempt
def addBuktiTransfer(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['bukti_transfer']:
        myfile = request.FILES['bukti_transfer']
        # print(myfile,type(myfile))
        # print(myfile.name, type(myfile.name))
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        buktiTransfer = BuktiTransfer(
            id_transaksi=request.POST['id_transaksi'],
            namaFile=myfile.name,
            urlFoto=uploaded_file_url
        )
        buktiTransfer.save()
        print("simpan bukti trr")
        return thankyouKonfirmasi(request)
    return konfirmasi(request)



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
