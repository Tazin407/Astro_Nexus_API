
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .import models
from django.contrib.auth.password_validation import validate_password

User= get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    password= serializers.CharField(label='Password',  style={'input_type': 'password'})
    confirm_password= serializers.CharField(label='Confirm_Password', style={'input_type': 'password'})

    class Meta:
        model= User
        fields= ['first_name', 'last_name','username','email','password','confirm_password', 'bio']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'confirm_password': 'Confirm Password',
            'bio': 'Add a bio',
        }
        
    def save(self):
        first_name= self.validated_data['first_name']
        last_name= self.validated_data['last_name']
        username= self.validated_data['username']
        email= self.validated_data['email']
        password= self.validated_data['password']
        confirm_password= self.validated_data['confirm_password']
        bio= self.validated_data['bio']
        
        if password!= confirm_password:
            raise serializers.ValidationError({"error": "Password didn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"error": "A user with this email already exists."}
            )
            
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"error": "Account with this username already exists."}
            )
            
        account = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            bio=bio,
        )
        account.set_password(password)
        account.save()
        return account

    
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, style={'input_type': 'password'} )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    confirm_password = serializers.CharField(required=True)

    def save(self, **kwargs):
        password1 = self.validated_data["new_password"]
        password2 = self.validated_data["confirm_password"]

        if password1 != password2:
            raise serializers.ValidationError({"error": "Password didn't match"})

        return super().save(**kwargs)