from django.db import models

# Create your models here.

class Category(models.Model):
    """
    A model for each individual categoory of products
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """
    A model for each individual brand of products
    """
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    A model for the individual products
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_code = models.CharField(max_length=254, null=True, blank=True)
    image_src = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
