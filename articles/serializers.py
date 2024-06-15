from rest_framework import serializers
from .import models

class ArticleSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= models.Article
        fields= '__all__'
        
class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Missions
        fields= '__all__'
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Likes
        fields= '__all__'