"""views_urls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('camera/', views.camera, name='camera'),
    path('courses/', views.courses, name='courses'),
    path('elementary/', views.elementary, name='elementary'),
    path('advanced/', views.advanced, name='advanced'),
    path('rates/', views.rates, name='rates'),
    path('contact/', views.contact, name='contact'),
    path('result/', views.result, name='result'),
    path('ML_prediction/', views.ML_prediction, name='ML_prediction'),
    #path('ML_output/', views.ML_output, name='ML_output'),
]
