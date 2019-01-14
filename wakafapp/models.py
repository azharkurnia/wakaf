from django.db import models

# Create your models here.
class CarouselPortofolio(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()


class FotoDonasi(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()


class Donatur(models.Model):
    nominal = models.IntegerField(blank=False)
    nama = models.CharField(max_length=140, blank=False)
    email = models.EmailField(max_length=140, blank=False)
    noHp = models.CharField(max_length=140, blank=False)
    kelamin = models.CharField(max_length=140, blank=False)
    birth = models.CharField(max_length=140, blank=False)
    alamat = models.CharField(max_length=300, blank=False)
    domisili = models.CharField(max_length=140, blank=False)
    id_transaksi = models.TextField(blank=False, default='null')
    kode_transfer = models.CharField(max_length=10, blank=False, default='null')
    created_on = models.DateTimeField(auto_now_add=True)


class Layanan(models.Model):
    judul = models.CharField(max_length=140, blank=False)
    konten = models.TextField(blank=False)


class Testimoni1(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()
    konten = models.TextField(blank=False)
    nama = models.TextField(max_length=140, blank=False)
    jabatan = models.TextField(max_length=140, blank=False)


class Testimoni2(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()
    konten = models.TextField(blank=False)
    nama = models.TextField(max_length=140, blank=False)
    jabatan = models.TextField(max_length=140, blank=False)


class Testimoni3(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()
    konten = models.TextField(blank=False)
    nama = models.TextField(max_length=140, blank=False)
    jabatan = models.TextField(max_length=140, blank=False)


class UnitBisnis(models.Model):
    namaFile = models.TextField(blank=False, default="null")
    urlFoto = models.URLField()
    judul = models.CharField(max_length=140, blank=False)
    konten = models.TextField(blank=False)
    indikator = models.TextField(default="null")

class Artikel(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()
    judul = models.CharField(max_length=140, blank=False)
    konten_short = models.TextField(max_length=400, blank=False)
    konten = models.TextField(blank=False)
    tags = models.CharField(max_length=20)


class ArtikelRekomendasi(models.Model):
    parent = models.ForeignKey(Artikel, blank=False, default=None)

class KegiatanVolunteer(models.Model):
    namaFile = models.TextField(blank=False)
    urlFoto = models.URLField()
    judul = models.CharField(max_length=140, blank=False)
    konten_short = models.TextField(max_length=400, blank=False)
    konten = models.TextField(blank=False)
    tags = models.CharField(max_length=20)


class Volunteer(models.Model):
    kegiatan = models.CharField(max_length=140, blank=False)
    nama = models.CharField(max_length=140, blank=False)
    email = models.EmailField(max_length=140, blank=False)
    noHp = models.CharField(max_length=140, blank=False)
    kelamin = models.CharField(max_length=140, blank=False)
    birth = models.CharField(max_length=140, blank=False)
    alamat = models.TextField(blank=False)
    domisili = models.CharField(max_length=140, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

class DonasiCMS(models.Model):
    title = models.CharField(max_length=140, blank=False, default='null')
    konten = models.TextField(blank=False, default='null')

class Parent(models.Model):
    nama = models.TextField(blank=False)


class Child(models.Model):
    parent = models.ForeignKey(Parent, blank=False, )
    value = models.TextField(max_length=10, blank=False)
