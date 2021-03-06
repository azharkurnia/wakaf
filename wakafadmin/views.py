from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
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
import random, string

response = {}


def show_login(request):
    return render(request, 'login.html', response)


@login_required
def tables(request):
    donaturList = Donatur.objects.all()
    response['donaturList'] = donaturList
    response['volunteerList'] = Volunteer.objects.all()
    # pesan = 'Test email wakaf'
    # email = EmailMessage(
    #     'Hello azhar',
    #     pesan,
    #     'info@wakaf.paii.co.id',
    #     ['azharkurnia19@gmail.com'],
    #     headers={'Message-ID': 'foo'}
    # )
    # email.send(fail_silently=False)
    #
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
def deleteFotoDonasi(request, foto_id):
    fs = FileSystemStorage()
    foto = FotoDonasi.objects.get(pk=foto_id)
    fs.delete(foto.namaFile)
    foto.delete()
    return redirect('wakafadmin:pageFotoDonasi')

@login_required
def deleteDonasiCMS(request, cms_id):
    cms = DonasiCMS.objects.get(pk=cms_id)
    cms.delete()
    return redirect('wakafadmin:pageFotoDonasi')


@login_required
@csrf_exempt
def uploadDonasiCMS(request):
    if (DonasiCMS.objects.count() > 0):
        DonasiCMS.objects.all().delete()
        print("hapus")

        if(request.method == 'POST'):
            judul = request.POST['judul']
            konten = request.POST['konten']

            deskripsi = DonasiCMS(
                title=judul,
                konten=konten
            )
            deskripsi.save()
            print("simpan")
    else:
        if(request.method == 'POST'):
            judul = request.POST['judul']
            konten = request.POST['konten']

            deskripsi = DonasiCMS(
                title=judul,
                konten=konten
            )
            deskripsi.save()
            print("simpan")
    return redirect('wakafadmin:pageFotoDonasi')

@login_required
def pageFotoDonasi(request):
    fotoDonasi = FotoDonasi.objects.all()
    response['fotoDonasi'] = fotoDonasi
    response['cmsDonasi'] = DonasiCMS.objects.all()
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
    return redirect('wakafadmin:pageCarouselHome')

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

@login_required
def pageArtikel(request):
    response['listArtikel'] = Artikel.objects.all()
    response['listArtikelRekomendasi'] = ArtikelRekomendasi.objects.all()

    return render(request,'pageArtikel.html',response)

@login_required
@csrf_exempt
def addArtikel(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['fotoArtikel']:
        myfile = request.FILES['fotoArtikel']
        judul = request.POST['nama']
        konten = request.POST['konten']
        preview = request.POST['preview']
        tag = request.POST['tag']

        # print(myfile.name, type(myfile.name))
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        artikel = Artikel(
            namaFile=myfile.name,
            urlFoto=uploaded_file_url,
            judul=judul,
            konten=konten,
            tags=tag,
            konten_short=preview,

        )
        artikel.save()
        print("simpan program")
    return redirect('wakafadmin:pageArtikel')

@login_required
@csrf_exempt
def addArtikelRekomendasi(request):
    if request.method == 'POST':
        artikel_id = request.POST['artikel']
        artikel = ArtikelRekomendasi(
            parent=Artikel.objects.get(pk=artikel_id)
        )
        artikel.save()
    return redirect('wakafadmin:pageArtikel')


@login_required
def deleteArtikel(request, artikel_id):
    fs = FileSystemStorage()
    artikel = Artikel.objects.get(pk=artikel_id)
    fs.delete(artikel.namaFile)
    artikel.delete()
    return redirect('wakafadmin:pageArtikel')

@login_required
def deleteArtikelRekomendasi(request, artikel_id):
    artikel = ArtikelRekomendasi.objects.get(pk=artikel_id)
    artikel.delete()
    return redirect('wakafadmin:pageArtikel')

@login_required
def pageKegiatanVolunteer(request):
    response['listKegiatan'] = KegiatanVolunteer.objects.all()
    return render(request,'pageKegiatanVolunteer.html',response)

@login_required
@csrf_exempt
def addKegiatanVolunteer(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['fotoKegiatan']:
        myfile = request.FILES['fotoKegiatan']
        judul = request.POST['nama']
        konten = request.POST['konten']
        preview = request.POST['preview']
        tag = request.POST['tag']
        # print(myfile.name, type(myfile.name))
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        kegiatan = KegiatanVolunteer(
            namaFile=myfile.name,
            urlFoto=uploaded_file_url,
            judul=judul,
            konten=konten,
            tags=tag,
            konten_short=preview,
        )
        kegiatan.save()
        print("simpan program")
    return redirect('wakafadmin:pageKegiatanVolunteer')

@login_required
def deleteKegiatanVolunteer(request, kegiatan_id):
    fs = FileSystemStorage()
    kegiatan = KegiatanVolunteer.objects.get(pk=kegiatan_id)
    fs.delete(kegiatan.namaFile)
    kegiatan.delete()
    return redirect('wakafadmin:pageKegiatanVolunteer')

@login_required
def paymentTables(request):
    donatur = Donatur.objects.all()
    bukti = BuktiTransfer.objects.all()
    response['donaturList'] = donatur
    response['buktiList'] = bukti
    return render(request, 'payment_table.html', response)

@login_required
def paidSlide(request, paid_id):
    print("slidepaid")
    payment = Donatur.objects.get(pk=paid_id)
    if (payment.payment):
        payment.payment = False
        payment.save()
        print("false")
    else:
        payment.payment = True
        print("true")
        payment.save()
        print("saved " + paid_id)
        # blast email
        idTransaksi = payment.id_transaksi
        emailUser = payment.email
        namaPeserta = payment.nama
        kelamin = payment.kelamin
        donasi = payment.jumlah_donasi
        pesan = "Assalamu'alaikum Warrahmatullahi Wabarakaatuh \n"\
                + 'Konfirmasi donasi ' + kelamin + ' ' + namaPeserta +' telah kami terima dan berikut kami sampaikan kuitansi pembayaran donasi dengan rincian:\n\n' \
                + 'Kuitansi Donasi\n' \
                + 'Nama Lengkap: ' + namaPeserta + '\n' + 'Nomor Transaksi: ' + idTransaksi + '\n' \
                + 'Total Donasi: Rp ' + str(donasi) + '\n\n' \
                + 'Jazakumullah khairan katsiran. Wa jazakumullah ahsanal jaza\n' \
                + '“Semoga Allah SWT akan membalas kamu dengan kebaikan yang banyak dan semoga Allah SWT membalas kamu dengan balasan yang terbaik”\n' \
                + 'Kami mengucapkan terimakasih atas kepercayaan '+ kelamin + ' kepada yayasan kami.\n' \
                + 'Insya Allah dengan donasi yang '+ kelamin + ' berikan akan kami teruskan kepada masyarakat yang membutuhkan.\n'\
                + 'Anda dapat mengetahui dan memantau program kami lebih lanjut disini http://wakaf.paii.co.id/program\n\n' \
                + 'Keterangan:\n' \
                + 'Kuitansi donasi ini berfungsi sebagai lampiran SPT Tahunan Pajak Penghasilan, untuk pengurang Penghasilan Kena Pajak (PKP), sesuai dengan Peraturan Direktur Jendral Pajak Nomor PER-6/PJ/2011 dan Nomor PER-15/PJ/2012.\n\n' \
                + "Wassalamu'alaikum Warrahmatullahi Wabarakaatuh\n" \
                + 'Tertanda,\n' + 'Muhammad Shaddam \n' +'Keuangan Yayasan Wakaf Produktif – Pengelola Aset Islami Indonesia'
        email = EmailMessage(
            'Pembayaran Donasi Berhasil Diverifikasi',
            pesan,
            'info@wakaf.paii.co.id',
            [emailUser],
            headers={'Message-ID': 'foo'}
        )
        email.send(fail_silently=False)
        print("email sent")
    return render(request, 'payment_table.html', response)


@login_required
def resend(request, paid_id):
    print("resend")
    payment = Donatur.objects.get(pk=paid_id)
    payment.payment = True
    print("true")
    payment.save()
    print("saved " + paid_id)
    # blast email
    idTransaksi = payment.id_transaksi
    emailUser = payment.email
    namaPeserta = payment.nama
    kelamin = payment.kelamin
    donasi = payment.jumlah_donasi
    pesan = "Assalamu'alaikum Warrahmatullahi Wabarakaatuh \n" \
            + 'Konfirmasi donasi ' + kelamin + ' ' + namaPeserta + ' telah kami terima dan berikut kami sampaikan kuitansi pembayaran donasi dengan rincian:\n\n' \
            + 'Kuitansi Donasi\n' \
            + 'Nama Lengkap: ' + namaPeserta + '\n' + 'Nomor Transaksi: ' + idTransaksi + '\n' \
            + 'Total Donasi: Rp' + str(donasi) + '\n\n' \
            + 'Jazakumullah khairan katsiran. Wa jazakumullah ahsanal jaza\n' \
            + '“Semoga Allah SWT akan membalas kamu dengan kebaikan yang banyak dan semoga Allah SWT membalas kamu dengan balasan yang terbaik”\n' \
            + 'Kami mengucapkan terimakasih atas kepercayaan ' + kelamin + ' kepada yayasan kami.\n' \
            + 'Insya Allah dengan donasi yang ' + kelamin + ' berikan akan kami teruskan kepada masyarakat yang membutuhkan.\n' \
            + 'Anda dapat mengetahui dan memantau program kami lebih lanjut disini http://wakaf.paii.co.id/program\n\n' \
            + 'Keterangan:\n' \
            + 'Kuitansi donasi ini berfungsi sebagai lampiran SPT Tahunan Pajak Penghasilan, untuk pengurang Penghasilan Kena Pajak (PKP), sesuai dengan Peraturan Direktur Jendral Pajak Nomor PER-6/PJ/2011 dan Nomor PER-15/PJ/2012.\n\n' \
            + "Wassalamu'alaikum Warrahmatullahi Wabarakaatuh\n" \
            + 'Tertanda,\n' + 'Muhammad Shaddam \n' + 'Keuangan Yayasan Wakaf Produktif – Pengelola Aset Islami Indonesia'
    email = EmailMessage(
        'Pembayaran Donasi Berhasil Diverifikasi',
        pesan,
        'info@wakaf.paii.co.id',
        [emailUser],
        headers={'Message-ID': 'foo'}
    )
    email.send(fail_silently=False)
    print("email sent")
    return render(request, 'payment_table.html', response)


