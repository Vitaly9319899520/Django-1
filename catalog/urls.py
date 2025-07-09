from django.urls import path
from catalog.apps import CatalogConfig
#from catalog.views import home, contacts
from catalog.views import CatalogListView, CatalogDetailView, CatalogView, CatalogUpdateView, CatalogDeleteView, \
    CategoryCreateView, CategoryUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
    path('category/new/', CategoryCreateView.as_view(),name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(),name='category_update'),
    path('',CatalogListView.as_view(), name='catalog_list'),
    path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='catalog_detail'),
    path('catalog/create', CatalogView.as_view(), name='catalog_create'),
    path('catalog/<int:pk>/update/', CatalogUpdateView.as_view(), name='catalog_update'),
    path('catalog/<int:pk>/delete/', CatalogDeleteView.as_view(), name='catalog_delete')

]


