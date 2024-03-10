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
        print(data)
        email = data.get("email")
        password = data.get("password")
        try:
            user = User.objects.get(email=email)
            print(user)
            if user.check_password(password):
                data['user'] = user
                print(data)
        except User.DoesNotExist:
            raise serializers.ValidationError('User Not Found')
        return data