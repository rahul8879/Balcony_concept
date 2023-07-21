from django.contrib import admin

from .models import Product

# Register your models here.

class ProductDetails(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('name',)
    }
admin.site.register(Product,ProductDetails)