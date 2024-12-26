from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .import models
from .import serializers
from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, UpdateAPIView

#email
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from django.contrib import messages

User= get_user_model()

class All_Users(ModelViewSet):
    queryset= User.objects.all()
    serializer_class= serializers.UserSerializer
    
   
class RegistrationView(ModelViewSet):
    queryset=  User.objects.none()
    serializer_class= serializers.RegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()
        token, _ = Token.objects.get_or_create(user=new_user)
        print("token created")
        
        if new_user.email_is_verified == False:
            current_site= get_current_site(request)
            user= new_user
            uid= urlsafe_base64_encode(force_bytes(user.pk))
            token= account_activation_token.make_token(user)
            print(uid, token)
            email= user.email
            subject= "Verify Your Email Address"
            message = render_to_string('verifyEmail.html', {
            'request': request,
            'user': user,
            'domain': current_site.domain,
            'uid': uid,
            'token': token,
            })
                
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            print('Email should be sent')
            return Response('Please Check Your Email')
                
        else:  
            print(serializer.errors)
        return Response(serializer.errors)
        
    
    
    
def activate(request, uidb64, token):
    print(uidb64, token)
    
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user= None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified=True 
        user.save()
        # messages.success(request,'Your account has been verified successfully')
        return redirect('login')
    
    return HttpResponse('This email has been verified already')


class LoginView(APIView):
    permission_classes=[AllowAny]
    serializer_class= serializers.LoginSerializer
    queryset= User.objects.none()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(email=email, password=password)
        if user:
            if user.email_is_verified:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                print(user.auth_token)
                return Response({"token": token.key, "user_id": user.id})
            else:
                return Response({'error': 'Please click on the link sent to your email'})
        else:
            return Response({"error": "Invalid Username or Password"})
    
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        self.request.user.auth_token.delete()
        logout(request)
        return Response('Logged out successfully')