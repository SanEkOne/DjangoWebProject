from django.urls import path
from . import views

app_name = 'store' 

urlpatterns = [
    path('', views.index, name='index'), 
    path('product_form/', views.product_form, name='product_form'),
    path('products/', views.products_list, name='api_products_list'),
]
