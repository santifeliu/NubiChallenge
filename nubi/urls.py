from django.urls import include
from django.urls import re_path
from .views import users as user_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Django REST Framework
from rest_framework.routers import SimpleRouter

schema_view = get_schema_view(
   openapi.Info(
      title="Nubi",
      default_version='v1',
      description="Nubi users challenge",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)


router = SimpleRouter()
router.register(r'', user_views.UserViewSet, basename='users')

urlpatterns = [

   # API docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
       name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path('users/', include(router.urls))
]
