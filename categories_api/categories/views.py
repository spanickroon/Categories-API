from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CategoriesCreateSerializer


# Create your views here.


class CategoriesCreateViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriesCreateSerializer
