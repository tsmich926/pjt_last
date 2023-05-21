from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Director,Actor,Movie,Genre

# Create your models here.
class User(AbstractUser):
    point = models.IntegerField(default=0)
    profile_path = models.TextField(null=True)
    theme= models.CharField(default="default",max_length=50)
    followings=models.ManyToManyField('self',symmetrical=False, related_name='followers')
    
    movies=models.ManyToManyField(Movie, related_name='like_users', blank=True)
    actors=models.ManyToManyField(Actor, related_name='like_users', blank=True)
    directors=models.ManyToManyField(Director, related_name='like_users', blank=True)
    genres=models.ManyToManyField(Genre, related_name='like_users', blank=True)
