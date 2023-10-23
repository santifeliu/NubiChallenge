# Models
from nubi.models import User

# Django REST Framework
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'last_name',
            'sex_type',
            'dni',
            'birth_date',
            'created_at'
        ]