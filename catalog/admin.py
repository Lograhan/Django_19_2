from django.contrib import admin
from .models import Category, Product, Version


# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'c_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_price', 'p_category',)
    list_filter = ('p_category',)
    search_fields = ('p_name', 'p_description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('v_prod', 'num_version', 'name', 'is_active',)