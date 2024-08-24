#urls de la aplicación biblioteca
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vender/', views.vender, name='vender'),
    path('prestar_libro/', views.prestar_libro, name='prestar_libro'),
    path('leer/<int:num1>/<int:num2>/', views.leer, name='leer'),  # ruta para leer libros con parámetro de página.
    path('sumadora/', views.sumadora, name='sumadora'), 
    path('suma/', views.suma, name='suma'),  # ruta para sumar dos números.  # ruta para sumar dos números.
]


