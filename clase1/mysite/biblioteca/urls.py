#urls de la aplicación biblioteca
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
