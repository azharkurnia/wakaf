from django.db import models

# Create your models here.
class CarouselPortofolio (models.Model):
    urlFoto = models.URLField

class FotoDonasi (models.Model):
    urlFoto = models.URLField

class Donatur(models.Model):
    nominal = models.IntegerField(blank=False)
    namaDepan = models.CharField(max_length=140, blank=False)
    namaBelakang = models.CharField(max_length=140, blank=False)
    email = models.EmailField(max_length=140, blank=False)
    noHp = models.CharField(max_length=140, blank=False)
    kelamin = models.CharField(max_length=140, blank=False)
    birth = models.CharField(max_length=140, blank=False)
    alamat = models.CharField(max_length=300, blank=False)
    domisili = models.CharField(max_length=140, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

class Layanan (models.Model):
    konten = models.TextField(blank=False)

class Testimoni (models.Model):
    foto = models.URLField
    konten = models.TextField(blank=False)
    nama = models.TextField(max_length=140, blank=False)
    jabatan = models.TextField(max_length=140, blank=False)

class UnitBisnis (models.Model):
    foto = models.URLField
    judul = models.CharField(max_length=140, blank=False)
    konten = models.TextField(blank=False)

class Volunteer (models.Model):
    kegiatan = models.CharField(max_length=140, blank=False)
    namaDepan = models.CharField(max_length=140, blank=False)
    namaBelakang = models.CharField(max_length=140, blank=False)
    email = models.EmailField(max_length=140, blank=False)
    noHp = models.CharField(max_length=140, blank=False)
    kelamin = models.CharField(max_length=140, blank=False)
    birth = models.CharField(max_length=140, blank=False)
    alamat = models.TextField(blank=False)
    domisili = models.CharField(max_length=140, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

class Parent (models.Model):
    nama = models.TextField

class Child (models.Model):
    nama = models.ForeignKey(Parent)
    value = models.IntegerField


