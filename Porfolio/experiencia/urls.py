from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiencia_list, name='experiencia_list'),
    path('agregar/', views.agregar_experiencia, name='agregar_experiencia'),
    path('editar/<int:pk>/', views.editar_experiencia, name='editar_experiencia'),
    path('eliminar/<int:pk>/', views.eliminar_experiencia, name='eliminar_experiencia'),
]
