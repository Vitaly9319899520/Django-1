from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_catalog_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'catalog_list'
    catalog = cache.get(key)
    if catalog is not None:
        return catalog
    catalog = Product.objects.all()
    cache.set(key, catalog)
    return catalog
