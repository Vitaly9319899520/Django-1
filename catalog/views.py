from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category


# def home(request):
#     return render(request,'home.html')
#
# def contacts(request):
#     return render(request,'contacts.html')

class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

# def catalog_list(request):
#     catalog = Product.objects.all()
#     context = {'catalog': catalog}
#     return render(request,'catalog_list.html', context)

class CatalogDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

# def catalog_detail(request, pk):
#     catalog = get_object_or_404(Product,pk=pk)
#     context = {'Product': catalog}
#     return render(request, 'product_detail.html', context)

class CatalogView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')

class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')

class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

