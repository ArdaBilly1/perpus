from django.db import models

class Kelompok(models.Model):
    nama = models.CharField(max_length=25)
    keterangan = models.CharField(max_length=60)

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=50) 
    penulis = models.CharField(max_length=50) 
    penerbit = models.CharField(max_length=50) 
    jumlah = models.IntegerField(null=True)
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul

