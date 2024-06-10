from django.contrib import admin
from .import models

admin.site.register(models.Article)
admin.site.register(models.Missions)
admin.site.register(models.Likes)
# Register your models here.
