from django.urls import path
from . import views


urlpatterns = [
 #  path('enero', views.index)
    path('', views.index),
    path('<month>', views.monthly_challenge),
]   
