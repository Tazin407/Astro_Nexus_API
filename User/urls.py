from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views


# router.register('register',views.RegistrationView)

# router.register('users',views.UserRegistrationViewset, basename= 'registration')

# router.register("list", UserViewset, basename="all-users")
# router.register("basic-info", UserBasicEditViewset, basename="user-basic-info")
router = DefaultRouter()
router.register("register", views.RegistrationView, basename="register-user")
router.register("users", views.All_Users, basename="all-users")
urlpatterns = [
    path("", include(router.urls)),
    path('activate/<uidb64>/<token>', views.activate,name='activate' ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("change-password/", UserChangePassword.as_view(), name="change-password"),
]

# urlpatterns = [
    
#     path('register/', views.RegistrationView.as_view(), name='register'),
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
#    
# ]