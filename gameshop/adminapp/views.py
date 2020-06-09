from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from authnapp.forms import ShopUserRegisterForm
from authnapp.models import ShopUser
from adminapp.forms import ProductEditForm, ProductCategoryEditForm, ShopUserAdminEditForm
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    response = redirect("admin:users")
    return response


class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = "adminapp/users.html"


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = "Создание нового пользователя"

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = "Редактирование пользователя"

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = "Удаление пользователя"

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = "Категории"

    categories_list = ProductCategory.objects.all()

    content = {
        "title": title,
        "categories": categories_list,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, 'adminapp/categories.html', content)


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"
    foo = "bar"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context["title"] = "категории/редактирование"
        return context


class ProductCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy("admin:categories")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk, page="1"):
    title = "Продукты"

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    paginator = Paginator(products_list, "2")
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page("1")
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content = {
            "title": title,
            "category": category,
            "objects": products_paginator,
            "media_url": settings.MEDIA_URL,
        }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = "Добавление продукта"
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse("admin:products", args=[pk]))
    else:
        product_form = ProductEditForm(initial={"category": category})

    content = {"title": title, "update_form": product_form, "category": category, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/product_update.html", content)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "adminapp/product_read.html"


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = "Редактирование продукта"
    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:product_update", args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {
        "title": title,
        "update_form": edit_form,
        "category": edit_product.category,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "adminapp/product_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = "Удаление продукта"

    product_to_delete = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_to_delete.is_active = False
        product_to_delete.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product_to_delete.category.pk]))

    content = {'title': title, 'product_to_delete': product_to_delete, "media_url": settings.MEDIA_URL}

    return render(request, 'adminapp/product_delete.html', content)

