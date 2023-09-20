from django.shortcuts import render
from catalog.models import Category, Product, Version
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory


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


class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:category')


class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_update_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        cotext_data = self.get_context_data()
        formset = cotext_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')
    template_name = 'main/product_confirm_delete.html'
