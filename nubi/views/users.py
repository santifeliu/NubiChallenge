# Django REST Framework
from rest_framework import viewsets

# Serializers
from nubi.serializers import UserModelSerializer

# Models
from nubi.models import User

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer