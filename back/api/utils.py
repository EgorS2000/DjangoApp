from django.http import HttpResponse
from rest_framework import permissions


def is_user_auth(func):
    def check(request):
        if not request.user:
            return HttpResponse(
                "You're not auth",
                content_type="application/json",
                status=403
            )
        return func(request)
    return check


class APIPermission(permissions.BasePermission):
    message = 'Only Egor can access APIs'

    def has_permission(self, request, view):
        return request.user.name == 'egor'


def serialization(**kwargs):
    serializer = kwargs.get('serializer')

    if kwargs.get('mode') == 'create' or 'get':
        serialized_data = serializer(data=kwargs.get('data'))

    if kwargs.get('mode') == 'update':
        serialized_data = serializer(
            instance=kwargs.get('instance'),
            data=kwargs.get('data')
        )

    if serialized_data.is_valid():
        serialized_data.save()

    return serialized_data
