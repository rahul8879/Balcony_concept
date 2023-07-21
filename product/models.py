from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    short_desc = models.TextField()
    material = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    installation_process = models.TextField()
    additional_benefits = models.TextField()
    image = models.ImageField(upload_to='product/', blank=True)

    def get_url(self):
        return reverse('package_details', args={self.slug
                                                })

    def __str__(self):
        return self.name
