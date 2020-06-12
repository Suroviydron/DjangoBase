from django.urls import re_path
from .apps import BasketappConfig

import basketapp.views as basketapp

app_name = BasketappConfig.name

urlpatterns = [
    re_path(r"^$", basketapp.basket, name="view"),
    re_path(r"^add/(?P<pk>\d+)/$", basketapp.basket_add, name="add"),
    re_path(r"^remove/(?P<pk>\d+)/$", basketapp.basket_remove, name="remove"),
    re_path(r"^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$", basketapp.basket_edit, name="edit"),
]
