from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views
from User.views import All_Users

router = DefaultRouter()
router.register('All_Users',All_Users)
router.register('Articles',views.ArticleView)
router.register('Mission',views.MissionView, basename='mission')
router.register('Likes',views.LikeView, basename='likes')
router.register('Liked_list',views.LikedListView, basename='liked_list')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.ArticleView.as_view({'get': 'list'})),
]
