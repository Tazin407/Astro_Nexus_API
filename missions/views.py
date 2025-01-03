from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .import serializers
from .import models
from .import static_data
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .import static_data

user= get_user_model()


class PlanetView(APIView):
    def get(self, request):
        return Response(static_data.planets)

class MissionView(ModelViewSet):        
    serializer_class= serializers.MissionSerializer
    queryset= models.Mission.objects.all()
    
    

class SaveMissionView(APIView):
    serializer_class= serializers.SaveMissionSerializer
    queryset=models.SaveMission.objects.all()
    
    def get(self, request):
        missions = models.SaveMission.objects.all()
        serializer = self.serializer_class(missions, many=True)  # Serialize multiple objects
        return Response(serializer.data)
    
    def post(self, request):
         #To solve AttributeError: 'SaveMissionView' object has no attribute 'user' I removed decorator
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(request):
            serializer.save(user=request.user)
            return Response(f"Saved successfully by {request.user}")
        return Response("Authenticate First")
    
    def delete(self, request, *args, **kwargs):
        user=request.user 
        mission_id = kwargs.get('mission_id')
        mission = models.SaveMission.objects.get(user=user, mission=mission_id)
        mission.delete()
        mission.save(user=request.user)
        return Response("Mission deleted")
    
    def get_queryset(self, request):
        queryset= models.SaveMission.objects.all()
        user= request.query_params.get('user_id')
        if user:
            queryset= models.SaveMission.objects.filter(user=user)
        return queryset
        
        
    

        