from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.home, name='result'),
    path('ML_prediction/', views.ML_prediction, name='ML_prediction'),
    #path('ML_output/', views.output_prediction, name='ML_output'),
]
