from rest_framework import serializers
# from .models import Loginmodel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields=['email','password']

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("User Not Found")
        data['user'] = user
        return data