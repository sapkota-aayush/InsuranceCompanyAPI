from rest_framework.pagination import PageNumberPagination

# Pagination for Customer
class CustomerPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
    
# Pagination for Policy
class PolicyPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
