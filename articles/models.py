from django.db import models
from User.models import CustomUser
# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=100)
    body= models.TextField()
    author= models.ForeignKey(CustomUser, related_name='articles', on_delete=models.CASCADE)
    date= models.DateField(auto_now_add=True)
    no_of_likes= models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
class Missions(models.Model):
    title= models.CharField(max_length=100)
    body= models.TextField()
    image= models.URLField(blank=True, null=True)
    date= models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
class Likes(models.Model):
    article= models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    
    def __str__(self) -> str:
        return f"Like on {self.article.title}"
