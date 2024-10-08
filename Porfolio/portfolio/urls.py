# portfolio/urls.py

from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='portfolio'),
  

   # Cambia "portfolio_view" a "home"
   
]
