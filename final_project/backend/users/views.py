from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .serializers import RegisterSerializer

# Create your views here.
class RegisterViews(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(ObtainAuthToken):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password'),
        )
        
        if not user:
            return Response(
                {'error': 'Credenciales inválidas'},
                status=status.HTTP_400_BAD_REQUEST
            ) 
            
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response(
            {
                'token': token.key
            }
        )