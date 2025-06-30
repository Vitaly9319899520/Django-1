from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


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

