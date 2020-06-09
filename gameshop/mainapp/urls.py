from django.urls import re_path
from .apps import MainappConfig

import mainapp.views as mainapp

app_name = MainappConfig.name

urlpatterns = [
   re_path(r"^$", mainapp.playstation, name='index'),
   re_path(r"^game/(?P<pk>\d+)/$", mainapp.playstation, name='game'),
]
