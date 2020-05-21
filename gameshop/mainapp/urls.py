
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.playstation, name='index'),
   path('game/<int:pk>/', mainapp.playstation, name='game'),
]
