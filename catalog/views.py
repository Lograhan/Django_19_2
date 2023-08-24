from django.shortcuts import render
from catalog.models import Category, Product


def index(request):
    all_category = Category.objects.all()
    context = {
        'object_list': all_category
    }
    return render(request, 'main/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'main/contacts.html')


def product(request):
    return render(request, 'main/product.html')


def category(request):
    return render(request, 'main/category.html')