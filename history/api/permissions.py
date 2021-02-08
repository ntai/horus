from rest_framework.permissions import BasePermission, SAFE_METHODS
from ..models import History

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    # my_safe_method = ['GET', 'PUT']
    # def has_permission(self, request, view):
    #     if request.method in self.my_safe_method:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj : History) -> bool:
        #member = Membership.objects.get(user=request.user)
        #member.is_active
        if request.method in SAFE_METHODS:
            return True
        # Note that obj.owner can be None
        return request.user.is_superuser or request.user.is_staff or request.user == obj.owner
    pass


class IsToken(BasePermission):
    message = 'You must be the staff of this project..'

    def has_object_permission(self, request, view, obj):
        #
        return request.user.is_superuser or request.user.is_staff

    pass

