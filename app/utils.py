import os

from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from django.core.exceptions import ImproperlyConfigured


# custom permissions for CRUD
class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


# exceptions for .env variables
def get_env_value(env_variable: object) -> object:
    try:
        return os.environ.get(env_variable)
    except KeyError:
        error_msg = f'Set the {env_variable} environment variable'
        raise ImproperlyConfigured(error_msg)
