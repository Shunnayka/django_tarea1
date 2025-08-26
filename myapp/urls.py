from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('nombre/', views.nombre_completo, name='nombre'),
]