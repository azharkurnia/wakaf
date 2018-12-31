from django.db import models

# Create your models here.
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

class FotoDonasi (models.Model):
    urlFoto = models.URLField

class Volunteer (models.Model):
    kegiatan = models.CharField(max_length=140, blank=False)
    namaDepan = models.CharField(max_length=140, blank=False)
    namaBelakang = models.CharField(max_length=140, blank=False)
    email = models.EmailField(max_length=140, blank=False)
    noHp = models.CharField(max_length=140, blank=False)
    kelamin = models.CharField(max_length=140, blank=False)
    birth = models.CharField(max_length=140, blank=False)
    alamat = models.CharField(max_length=300, blank=False)
    domisili = models.CharField(max_length=140, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

class CarouselPortofolio (models.Model):
    urlFoto = models.URLField

