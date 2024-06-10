from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views
from User.views import All_Users

router = DefaultRouter()
router.register(r'All_Users',All_Users)
router.register(r'Articles',views.ArticleView)
router.register(r'Mission',views.MissionView)
router.register(r'Likes',views.LikeView)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.ArticleView.as_view({'get': 'list'})),
]
