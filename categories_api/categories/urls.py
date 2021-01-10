from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CategoriesCreateViewSet.as_view({'post': 'create'})),
    path('<int:pk>/', views.CategoriesViewSet.as_view({'get': 'retrieve'})),
]
