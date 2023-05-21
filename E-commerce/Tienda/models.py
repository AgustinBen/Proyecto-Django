from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    slug = models.SlugField(default='', null=False )

    def __str__(self):
        return f'{self.nombre}({self.precio})'

    def get_url(self):
        return reverse('detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
