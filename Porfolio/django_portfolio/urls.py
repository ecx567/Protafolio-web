"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views 
from django.contrib.auth import urls

#from portfolio.views import ExperienciaListView, ExperienciaCreateView, ExperienciaUpdateView, ExperienciaDeleteView



urlpatterns = [
    path("admin/", admin.site.urls),
    path('',  views.home),
    path('blog/', include('blog.urls')),
    path('experiencia/', include('experiencia.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    

    #path('accounts/', include('accounts.urls')),
    #path('', include('portfolio.urls'))
    #path("signup/", views.signup, name="signup"),
    #path("signin/", views.signin, name="signing"),
    #path("logout/",views.signout, name="logout")
    #path('experiencias/', ExperienciaListView.as_view(), name='experiencia_list'),
    #path('experiencias/nueva/', ExperienciaCreateView.as_view(), name='experiencia_create'),
    #path('experiencias/<int:pk>/editar/', ExperienciaUpdateView.as_view(), name='experiencia_update'),
    #path('experiencias/<int:pk>/eliminar/', ExperienciaDeleteView.as_view(), name='experiencia_delete'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
