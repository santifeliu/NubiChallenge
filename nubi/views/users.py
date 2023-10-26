# Django REST Framework
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from nubi.serializers import UserModelSerializer

# Models
from nubi.models import User

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['email', 'sex_type']
    ordering_fields = ['email']