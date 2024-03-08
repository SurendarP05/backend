from rest_framework.views import APIView
from .serializer import LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status



class Login(APIView):
    def post(self, request):
       serializer = LoginSerializer(data=request.data)
       if not serializer.is_valid():
         print(serializer.errors)
         
       return Response('demo',)
    
    #    if serializer.is_valid():
    #         email = serializer.data['email']
    #         password = serializer.data['password']
    #         user = authenticate(email=email, password=password)
    #         print(user)
    #         if  user : 
    #          refresh = RefreshToken.for_user(user)
    #          return Response({
    #                 'access_token': str(refresh.access_token),
    #                 'refresh_token': str(refresh)
    #             }, status=status.HTTP_200_OK)
            
    #         else:
    #             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
     