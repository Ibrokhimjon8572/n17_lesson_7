from django.db import models

# Create your models here.
class Avto(models.Model):
    model = models.CharField(max_length=30, null=True, blank=True)
    price = models.IntegerField(default=10000)
    color = models.CharField(max_length=20, default='oq')
    year = models.CharField(max_length=30, default='2000')
    image = models.ImageField(upload_to='avto/static/images/', blank=True)

    def __str__(self) -> str:
        return self.model