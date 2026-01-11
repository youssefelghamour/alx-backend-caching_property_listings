# Django Property Listings with Redis Caching

This project implements a Django-based property listing application with Redis caching using various caching strategies including view-level caching, low-level queryset caching, and proper cache invalidation techniques.

The application uses Docker to containerize PostgreSQL for data persistence and Redis for caching.

- Multi-level caching with view-level and queryset-level strategies  
- Cache invalidation using Django signals  
- Containerized development with Docker  
- Monitoring Redis cache metrics (hits, misses, hit ratio) 

## Setup

1. Build and run containers:
```bash
docker-compose up --build
```
2. Apply migrations:
```bash
docker-compose exec web python manage.py migrate
```
3. (Optional) Create superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Example Endpoints

- `/properties/` : List all properties (cached)
- `/metrics/` : Retrieve Redis cache metrics (hits, misses, hit ratio)
- `/admin/` : Django admin panel