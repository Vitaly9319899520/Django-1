from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category

from django.contrib.auth.mixins import LoginRequiredMixin


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

class CatalogView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')


class CatalogUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')


    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.change_product'):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

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


@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = False
    product.save()

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description']  # укажи свои поля
    template_name = 'product/create_product.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца
        return super().form_valid(form)


