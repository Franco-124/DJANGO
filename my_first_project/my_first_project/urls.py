"""
URL configuration for my_first_project project.

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
from django.urls import path, include  # Asegúrate de importar 'include'
from my_first_app.views import car_list, author_list  # Importando las vistas

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('car_list/', car_list, name='car_list'),  # Ruta para la lista de carros
    path('autores/', author_list, name='author_list'),  # Ruta para la lista de autores
    path('Profile/', include('my_first_app.urls')),  # Incluir las URLs de la app 'my_first_app'
]