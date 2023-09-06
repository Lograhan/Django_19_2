from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product, category, products, product_category

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
    path('category/', category, name='category'),
    path('products/', products, name='products'),
    path('product_category/<int:pk>/', product_category, name='product_category'),
]
