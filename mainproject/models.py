from django.db import models
from django.utils import timezone

class Ogrenci(models.Model):
    SEVIYE_CHOICES = [
        ('A1', 'A1 - Başlangıç'),
        ('A2', 'A2 - Temel'),
        ('B1', 'B1 - Orta'),
        ('B2', 'B2 - İleri'),
        ('C1', 'C1 - Üst'),
        ('C2', 'C2 - Uzman'),
    ]
    
    ad_soyad = models.CharField(max_length=100)
    kayit_tarihi = models.DateField(default=timezone.now)
    seviye = models.CharField(max_length=3, choices=SEVIYE_CHOICES, default='A1')
    profil_foto = models.ImageField(upload_to='ogrenci_profil/', blank=True, null=True)
    ozel_notlar = models.TextField(blank=True, help_text="Öğretmen için özel notlar")
    ai_notlar = models.TextField(blank=True, help_text="Yapay zeka önerileri")
    son_guncelleme = models.DateField(auto_now=True)
    mevcut_cuz = models.PositiveSmallIntegerField(default=1)
    hedef_cuz = models.PositiveSmallIntegerField(default=30)
    puan = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 11)])  # 1-10 arası puan
    
    def __str__(self):
        return self.ad_soyad

class EzberKaydi(models.Model):
    ogrenci = models.ForeignKey(Ogrenci, on_delete=models.CASCADE, related_name='ezberler')
    tarih = models.DateField(default=timezone.now)
    baslangic_sayfa = models.PositiveSmallIntegerField()
    bitis_sayfa = models.PositiveSmallIntegerField()
    ezber_suresi = models.PositiveSmallIntegerField(help_text="Dakika cinsinden")
    ogretmen_notu = models.TextField(blank=True)
    
    def ilerleme(self):
        return self.bitis_sayfa - self.baslangic_sayfa
    
    def sayfa_basina_sure(self):
        if self.ilerleme() > 0:
            return round(self.ezber_suresi / self.ilerleme(), 2)
        return 0