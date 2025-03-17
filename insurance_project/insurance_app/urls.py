from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomerViewset, PolicyViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewset)
router.register(r'policies', PolicyViewSet)

# Include the router URLs
urlpatterns = [
    path('api/', include(router.urls)),  
    
    # JWT authentication endpoints
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #djoser endpoints
    path('auth/',include('djoser.urls')),#for registration,password reset etc
    path('auth/',include('djoser.urls.jwt')), #for jwt-based authentication with djoser
]
