from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=100)
    publisher = models.CharField(verbose_name="издатель", max_length=100, blank=True)
    developer = models.CharField(verbose_name="разработчик", max_length=100, blank=True)
    released = models.CharField(verbose_name="дата выхода", max_length=10, blank=True)
    platform = models.CharField(verbose_name="платформа", max_length=20, default="PS4")
    genre = models.CharField(verbose_name="жанр", max_length=50, blank=True)
    language = models.CharField(verbose_name="язык", max_length=30, default="Русский")
    age = models.CharField(verbose_name="возрастной рейтинг", max_length=10, default="18+")
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    price = models.DecimalField(verbose_name="цена", max_digits=8, decimal_places=0, default=0)
    quantity = models.PositiveIntegerField(verbose_name="остаток на складе", default=0)
    image01 = models.ImageField(upload_to='products_images', blank=True)
    image02 = models.ImageField(upload_to='products_images', blank=True)
    image03 = models.ImageField(upload_to='products_images', blank=True)
    image04 = models.ImageField(upload_to='products_images', blank=True)
    image05 = models.ImageField(upload_to='products_images', blank=True)
    image06 = models.ImageField(upload_to='products_images', blank=True)
    video_url = models.TextField(verbose_name="ссылка на видео", blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50, verbose_name="номер телефона")
    email = models.EmailField(max_length=254, verbose_name="электронная почта")
    city = models.CharField(max_length=128, default="Краснодар", verbose_name="город")
    address = models.CharField(max_length=254, verbose_name="адресс")

    def __str__(self):
        return f"{self.pk} {self.email}"