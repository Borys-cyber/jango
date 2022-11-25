from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    object = None
    name = models.CharField(max_length=200, help_text='Product name', default=None)
    price = models.FloatField(help_text='Product price', default=0)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.id = None

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])

