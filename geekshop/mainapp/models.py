from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    short_desc = models.TextField(verbose_name="краткое описание", max_length=60, blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    price = models.DecimalField(verbose_name="цена", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="остаток на складе", default=0)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50, verbose_name="номер телефона")
    email = models.EmailField(max_length=254, verbose_name="электронная почта")
    city = models.CharField(max_length=128, default="Москва", verbose_name="город")
    address = models.CharField(max_length=254, verbose_name="адресс")

    def __str__(self):
        return f"{self.pk} {self.email}"