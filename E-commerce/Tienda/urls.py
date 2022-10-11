from django.urls import path
from . import views


urlpatterns = [
    path('inicio/', views.index),
    path('inicio/lista-productos/', views.lista_productos),
    # path('<month>', views.monthly_challenge),
 ]   
