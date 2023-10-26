# Models
from nubi.models import User

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserModelSerializer(serializers.ModelSerializer):
    dni = serializers.RegexField(r'^\d+$', max_length=8, validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = [
            'wallet_id',
            'email',
            'name',
            'last_name',
            'sex_type',
            'dni',
            'birth_date',
            'created_at'
        ]
        read_only_fields = [
            'wallet_id',
            'created_at',
        ]