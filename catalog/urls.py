from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductCategoryListView, ProductListView, ProductDetailView, CategoryListView, \
    ProductsListView, ProductsCreateView, ProductsUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', never_cache(ProductsCreateView.as_view()), name='products_create'),
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products_category/<int:pk>/', ProductCategoryListView.as_view(), name='product_category'),
    path('update/<int:pk>', never_cache(ProductsUpdateView.as_view()), name='products_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='products_delete')
]
