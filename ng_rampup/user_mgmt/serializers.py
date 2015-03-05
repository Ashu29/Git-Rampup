from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from user_mgmt.models import MyUser
__author__ = 'ubuntu'
from rest_framework import serializers


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'username', 're_password')
        read_only_fields = ('username',)

    def create(self, validated_data):
        password = validated_data.get('password')
        re_password = validated_data.get('re_password')
        if not (password and re_password):
            raise ValidationError("Please provide a password")
        else:
            if password == re_password:
                validated_data.pop('re_password')
                return MyUser.objects.create_user(**validated_data)
            else:
                raise ValidationError("Passwords don't match")
