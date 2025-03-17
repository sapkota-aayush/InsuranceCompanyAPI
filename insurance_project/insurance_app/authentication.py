from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission


class IsManager(BasePermission):
    def has_permission(self,request,view):
        if request.method in ['GET']:
            return request.user.is_authenticated
        if request.user.is_authenticated:
            return request.user.groups.filter(name='Manager').exists()
        return False