from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CategoriesCreateSerializer, CategoriesSerializer
from .models import Category


class CategoriesCreateViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriesCreateSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CategoriesSerializer

    def get_queryset(self):
        category = Category.objects.all().filter(id=self.kwargs['pk'])
        return category
