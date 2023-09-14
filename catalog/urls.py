from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductCategoryListView, ProductListView, ProductDetailView, CategoryListView, ProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products_category/<int:pk>/', ProductCategoryListView.as_view(), name='product_category')
]
