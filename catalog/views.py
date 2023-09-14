from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    contex = {
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', contex)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'
    extra_context = {
        'title': 'Товар'
    }


class CategoryListView(ListView):
    model = Category
    template_name = 'main/category.html'


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'main/product_category.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(p_category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Товары категории {category_item.c_name}'
        return context_data


class ProductsListView(ListView):
    model = Product
    template_name = 'main/products.html'
