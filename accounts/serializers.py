from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from .models import Account, Role, Permission


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'password',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'roles',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        # Validate the new password using Django's password validation
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        # Hash the password before saving
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Remove password from validated_data to prevent updating it
        validated_data.pop('password', None)
        return super().update(instance, validated_data)

    def get_fields(self):
        fields = super().get_fields()

        # If this is an update operation, remove the password field
        if self.instance:
            fields.pop('password')

        return fields


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
