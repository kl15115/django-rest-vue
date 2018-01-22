from .models import Items
from .serializers import ItemsSerializer
from rest_framework import authentication, permissions, viewsets


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
     )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ItemViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""
    queryset = Items.objects.order_by('id')
    serializer_class = ItemsSerializer
