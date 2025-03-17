from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .models import Customer, Policy
from .serializers import CustomerSerializer, PolicySerializer
from .pagination import CustomerPagination, PolicyPagination
from .authentication import IsManager
from .sanitizer import sanitize



def sanitize_input_data(self, data):
    return sanitize(data) # calls the sanitize function from sanitizer.py

#All funtion below is import to store sanitized data in data as above function will sanitize the data but wont save that data in database
def create(self, request, *args, **kwargs): 
    sanitized_data = self.sanitize_input_data(request.data)
    return super().create(request, *args, **kwargs)

def update(self, request, *args, **kwargs):
    sanitized_data = self.sanitize_input_data(request.data)
    return super().update(request, *args, **kwargs)

def partial_update(self, request, *args, **kwargs):
    sanitized_data = self.sanitize_input_data(request.data)
    return super().partial_update(request, *args, **kwargs)



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
    filterset_fields = ['policy_type', 'customer__first_name']  # Specify fields to filter for Policy model
    search_fields = ['policy_type']  # Specify search fields for Policy model
    ordering_fields = ['coverage_amount']  # Specify ordering fields for Policy model
    pagination_class = PolicyPagination  # Overrides global setting

