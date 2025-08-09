from django.db import models
from django.utils.text import slugify
# Create your models here.
    
class category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class yazi(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='uploads', blank=True, null=True)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False,unique=True,db_index=True)
    tarih = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category,default=1, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f'{self.title} {self.date}'
