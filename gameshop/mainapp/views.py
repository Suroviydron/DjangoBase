
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket
from .models import Contact, Product, ProductCategory
from django.utils import timezone
import random
import datetime


def main(request):
    title = 'Главная'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {'title': title,  "basket": basket, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', content)

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def playstation(request, pk=None):
    title = "PlayStation"
    basket = get_basket(request.user)

    if pk is not None:
        product = get_object_or_404(Product, pk=pk)
        same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
        content = {
            "title": title,
            "product": product,
            "basket": basket,
            "same_products": same_products,
            "media_url": settings.MEDIA_URL,
        }
        return render(request, "mainapp/game_list.html", content)

    hot_product = get_hot_product()

    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    new_products = Product.objects.filter(category__pk=1)
    exclusive_products = Product.objects.filter(category__pk=2)
    cool_products = Product.objects.filter(category__pk=3)
    ubisoft_products = Product.objects.filter(category__pk=4)
    ea_products = Product.objects.filter(category__pk=5)
    content = {
        "title": title,
        "categories": categories,
        "products": products,
        "new_products": new_products,
        "exclusive_products": exclusive_products,
        "cool_products": cool_products,
        "ubisoft_products": ubisoft_products,
        "ea_products": ea_products,
        "hot_product": hot_product,
        "basket": basket,
        "media_url": settings.MEDIA_URL,
    }

    if pk:
        print(f"User select category: {pk}")

    return render(request, "mainapp/playstation.html", content)


def game_list(request, pk=None):

    if pk is not None:
        title = "Игра для PlayStation"
        basket = get_basket(request.user)
        product = get_object_or_404(Product, pk=pk)

    content = {
        "product": product,
        "title": title,
        "basket": basket,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, "mainapp/game_list.html.html", content)


def contact(request):
    title = "О нас"
    visit_date = datetime.datetime.now()
    information = Contact.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {"title": title, "visit_date": visit_date, "basket": basket, "information": information}
    return render(request, "mainapp/contact.html", content)

