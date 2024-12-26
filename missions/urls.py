from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('mission',views.MissionView, basename='mission')

# router.register('SaveMissionView', views.SaveMissionView, basename='save_mission')

urlpatterns = [
    path('', include(router.urls)),
    path('planets/', views.PlanetView.as_view()),
    path('savemission/', views.SaveMissionView.as_view()),
    path('missions/<int:mission_id>/delete/', views.SaveMissionView.as_view(), name='delete-mission'),
    # path('', views.ArticleView.as_view({'get': 'list'})),
]
