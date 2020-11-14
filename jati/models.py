from django.db import models

# Create your models here.


class Pengalaman(models.Model):
    cerita_pengalaman = models.CharField(max_length=1000)

    def __str__(self):
        return self.cerita_pengalaman
