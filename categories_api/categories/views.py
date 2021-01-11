"""The module in which the views of the category application are located."""

from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CategoriesCreateSerializer, CategoriesSerializer
from .models import Category


class CategoriesCreateViewSet(viewsets.ModelViewSet):
    """View set to create categories."""

    serializer_class = CategoriesCreateSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """View set for displaying categories."""

    serializer_class = CategoriesSerializer

    def get_queryset(self) -> object:
        """Method that overrides the standard method to get queryset."""
        category = Category.objects.all().filter(id=self.kwargs['pk'])
        return category
