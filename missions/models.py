from django.db import models
from django.contrib.auth import get_user_model
from .import static_data

user= get_user_model()

class Mission(models.Model):
    Title= models.CharField(max_length=100)
    Description= models.TextField()
    FullViewLink= models.URLField()
    Image= models.URLField()
    
    def __str__(self):
        return self.Title
    
class SaveMission(models.Model):
    user= models.ForeignKey(user, on_delete=models.CASCADE)
    mission= models.ForeignKey(Mission, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + self.user.last_name + " saved " + self.mission.Title

# class Comment(models.Model):
#     Mission= models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="comments")
#     User= models.ForeignKey(user, on_delete=models.CASCADE, related_name="comments")
#     Comment= models.TextField()
    
#     def __str__(self):
#         return self.User.first_name + self.user.last_name + " commented on " + self.Mission.Title