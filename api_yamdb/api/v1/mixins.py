from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from .permissions import AdminOrReadOnlyPermission


class GenreCategoryMixin(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """Общий класс для жанров и категорий"""
    permission_classes = (AdminOrReadOnlyPermission,)
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
