import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket
from .models import Contact, Product, ProductCategory


def main(request):
    title = 'Главная'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {'title': title,  "basket": basket, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', content)


def playstation(request, pk=None):
    title = "PlayStation"

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        product = get_object_or_404(Product, pk=pk)
        content = {
            "title": title,
            "product": product,
            "basket": basket,
            "media_url": settings.MEDIA_URL,
        }
        return render(request, "mainapp/game_list.html", content)

    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    newproducts = Product.objects.filter(category__pk=1)
    exclusiveproducts = Product.objects.filter(category__pk=2)
    coolproducts = Product.objects.filter(category__pk=3)
    ubiproducts = Product.objects.filter(category__pk=4)
    eaproducts = Product.objects.filter(category__pk=5)
    content = {
        "title": title,
        "categories": categories,
        "products": products,
        "newproducts": newproducts,
        "exclusiveproducts": exclusiveproducts,
        "coolproducts": coolproducts,
        "ubiproducts": ubiproducts,
        "eaproducts": eaproducts,
        "basket": basket,
        "media_url": settings.MEDIA_URL
    }

    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/playstation.html", content)


def contact(request):
    title = "О нас"
    visit_date = datetime.datetime.now()
    information = Contact.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {"title": title, "visit_date": visit_date, "basket": basket, "information": information}
    return render(request, "mainapp/contact.html", content)

