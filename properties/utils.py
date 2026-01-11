from django.core.cache import cache
from .models import Property


def get_all_properties():
    """Function to get all properties with caching"""
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.values())
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    return properties