from typing import Any
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .import models 
from .import serializers
from django.contrib.auth import get_user_model, get_user
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
 
# Create your views here.
User= get_user_model()

class ArticleView(ModelViewSet):
    serializer_class= serializers.ArticleSerializer
    queryset= models.Article.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):
        queryset= super().get_queryset()      
        id= self.request.query_params.get("author_id")
        approved= self.request.query_params.get("approved")

        if id:
            try:
                author= User.objects.get(id=id)
                if approved:
                    queryset= queryset.filter(author=author.id, approved=approved)
                queryset= queryset.filter(author=author.id)
                return queryset
            except User.DoesNotExist:
                return None
            
        return queryset
            
    
class MissionView(ModelViewSet):
    serializer_class= serializers.MissionsSerializer
    queryset= models.Missions.objects.all()
    
class LikeView(ModelViewSet):
    serializer_class= serializers.LikeSerializer
    queryset= models.Likes.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer= self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user= serializer.validated_data.get("user")
            article= serializer.validated_data.get("article")
            
            try:
                existingLike= models.Likes.objects.get(user=user,article=article)
                existingLike.delete()
                article.no_of_likes-=1
                article.save()
                return Response("like removed")
                
            except models.Likes.DoesNotExist:
                newLike= serializer.save()
                newLike.save()
                article.no_of_likes+=1
                article.save()
                return Response("liked")
            
        return Response(serializer.errors)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        liked= self.request.query_params.get("liked")
        article_id = self.request.query_params.get("article_id")
    
        if user_id:
            try:
                user = User.objects.get(id=user_id)   
                # queryset = queryset.filter(user=user)
                queryset= models.Article.objects.filter(likes__user=user_id)
                return queryset
            except User.DoesNotExist:
                return queryset.none()  

        # if article_id:
        #     try:
        #         article = models.Article.objects.get(id=article_id)  
        #         queryset = queryset.filter(article=article)
        #     except models.Article.DoesNotExist:
        #         return queryset.none()  

        return queryset

    
    
  