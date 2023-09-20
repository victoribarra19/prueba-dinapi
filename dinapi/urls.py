"""
URL configuration for dinapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from personas import views



urlpatterns = [
    path('', views.Inicio,name='Inicio'),
    path('admin/', admin.site.urls,name='admin/'),
    path('personas/',views.Personas,name='personas/'),
    path('editar_persona/<int:persona_id>/',views.editar_persona,name='editar_persona'),
    #path('eliminar_persona/<int:id>/',views.eliminar_persona,name='eliminar_persona'),
    path('eliminar_persona/<int:pk>/', views.EliminarPersonaView.as_view(), name='eliminar_persona')
]
