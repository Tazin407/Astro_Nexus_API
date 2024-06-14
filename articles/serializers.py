from rest_framework import serializers
from .import models

class ArticleSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= models.Article
        fields= ['title', 'body', 'image', 'author', 'approved']
        
class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Missions
        fields= ['title', 'body', 'image']
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Likes
        fields= '__all__'