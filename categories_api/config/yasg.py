from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title='Catagories API',
      default_version='v1',
      description="""A simple Categories API that stores category tree
      to databaseand returns category parents, children and siblings
      by category id.""",
      license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path(
      'redoc/', schema_view.with_ui('redoc', cache_timeout=0),
      name='schema-redoc'),
]
