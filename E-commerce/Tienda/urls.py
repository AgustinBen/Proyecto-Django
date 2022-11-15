from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index-page'),
    path('lista-productos/', views.lista_productos, name='lista-page'),
    path('producto/<slug:slug>', views.product_detail, name='producto-detail-page'),
    # path('<month>', views.monthly_challenge),
]   
