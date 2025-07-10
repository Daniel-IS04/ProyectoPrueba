from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="Este correo ya esta en uso")]
    )
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password2']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'error': 'las contraseñas no coinciden'}
            )  
        return attrs
    
    def create(self, validate_data):
        validate_data.pop('password2')
        
        return User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password']
        )