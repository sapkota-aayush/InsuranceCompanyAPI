from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .models import Customer, Policy
from .serializers import CustomerSerializer, PolicySerializer
from .pagination import CustomerPagination, PolicyPagination



# Base viewset with common filtering, searching, and ordering logic
class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = []  # List of fields to be searched
    ordering_fields = []  # List of fields to be ordered
    filterset_fields = []  # List of fields to be filtered
    
    # You can override these fields in your individual viewsets if needed

# Viewset for Customer
class CustomerViewset(BaseViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['first_name', 'last_name']  # Specify fields to filter for Customer model
    search_fields = ['last_name']  # Specify search fields for Customer model
    ordering_fields = ['first_name']  # Specify ordering fields for Customer model
    pagination_class = CustomerPagination  # Overrides global setting


# Viewset for Policy
class PolicyViewSet(BaseViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    filterset_fields = ['policy_number', 'customer__first_name']  # Specify fields to filter for Policy model
    search_fields = ['policy_number']  # Specify search fields for Policy model
    ordering_fields = ['policy_number']  # Specify ordering fields for Policy model
    pagination_class = PolicyPagination  # Overrides global setting

