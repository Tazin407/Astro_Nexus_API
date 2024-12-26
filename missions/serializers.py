
from rest_framework import serializers
from .models import SaveMission, Mission

class PlanetSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    link = serializers.URLField()
    image = serializers.URLField()
    
class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'
        
class SaveMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveMission
        fields = '__all__'
        
    def is_valid(self, request):
        valid= super().is_valid()
        if request.user.is_authenticated:
            return valid
        else:
            return False