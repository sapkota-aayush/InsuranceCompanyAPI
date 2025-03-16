from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insurance_app.urls')),  # Correct path to app URLs
]
