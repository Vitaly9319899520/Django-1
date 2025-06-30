from django.urls import path
from catalog.apps import CatalogConfig
#from catalog.views import home, contacts
from catalog.views import CatalogListView, CatalogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
    path('',CatalogListView.as_view(), name='catalog_list'),
    path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='catalog_detail')
]


