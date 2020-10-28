from django.db import models

# Create your models here.


class Kegiatan(models.Model):
    nama_kegiatan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kegiatan
