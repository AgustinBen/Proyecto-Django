from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index-page'),
    path('lista-productos/', views.lista_productos, name='lista-page'),
    path('<slug:slug>', views.detail, name='detail'),
]   

