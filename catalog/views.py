from django.shortcuts import render
from catalog.models import Category, Product


def index(request):
    all_product = Product.objects.all()
    context = {
        'object_list': all_product,
        'title': 'Главная'
    }
    return render(request, 'main/home.html', context)


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


def product(request, pk):
    contex = {
        'object_list': Product.objects.filter(id=pk),
        'title': 'Товар'
    }
    return render(request, 'main/product.html', contex)


def category(request):
    all_category = Category.objects.all()
    contex = {
        'object_list': all_category,
        'title': 'Категории'
    }
    return render(request, 'main/category.html', contex)


def product_category(request, pk):
    category_item = Category.objects.get(pk=pk)
    contex = {
        'object_list': Product.objects.filter(p_category_id=pk),
        'title': f'Товары категории {category_item.c_name}'
    }
    return render(request, 'main/product_category.html', contex)


def products(request):
    all_product = Product.objects.all()
    contex = {
        'object_list': all_product,
        'title': 'Товары'
    }
    return render(request, 'main/products.html', contex)


