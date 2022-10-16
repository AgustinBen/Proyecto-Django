from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('lista-productos/', views.lista_productos),
    # path('<month>', views.monthly_challenge),
]   
