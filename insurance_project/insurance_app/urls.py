from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewset, PolicyViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewset)  # Correct the case here
router.register(r'policies', PolicyViewSet)

# Include the router URLs
urlpatterns = [
    path('api/', include(router.urls)),  # Make sure to add the trailing slash
]
