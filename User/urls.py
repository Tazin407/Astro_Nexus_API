from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views


# router.register('register',views.RegistrationView)

# router.register('users',views.UserRegistrationViewset, basename= 'registration')

urlpatterns = [
    
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', views.activate,name='activate' )
]