from django.shortcuts import render
from .models import Property
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties


# @cache_page(60 * 15)  # Cache the view for 15 minutes in Redis
def property_list(request):
    # properties = list(Property.objects.values())
    properties = get_all_properties()
    return JsonResponse({"data": properties})