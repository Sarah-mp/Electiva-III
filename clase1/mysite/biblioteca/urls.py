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

    # crud de libros
    path('ver_libros/', views.ver_libros, name='ver_libros'),  # ruta para ver todos los libros.
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),  # ruta para eliminar un libro.
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),  # ruta para agregar un libro.

]


