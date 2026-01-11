from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging


logger = logging.getLogger(__name__)


def get_all_properties():
    """Function to get all properties with caching"""
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    return properties


def get_redis_cache_metrics():
    """Function to get Redis cache metrics"""
    redis_conn = get_redis_connection("default")  # use our default cache
    info = redis_conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    
    total = hits + misses
    # Ratio of how often our cache was used vs missed
    hit_ratio = hits / total if total > 0 else 0.0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio
    }

    logger.info(f"Redis cache metrics: {metrics}")
    return metrics