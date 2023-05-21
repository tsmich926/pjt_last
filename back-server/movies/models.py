from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
# Create your models here.
# id를 data 가공에서 pk로 전부 바꿔주었음.

class Actor(models.Model):
    # id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    profile_path=models.TextField(null=True)
    gender=models.IntegerField()


    # likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)

class Director(models.Model):
    # id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    profile_path=models.TextField(null=True)
   
   
    # likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)

class Genre(models.Model):
    # id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
   
   
    # likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)

class Movie(models.Model):
    # id=models.IntegerField(unique=True,primary_key=True)
    title=models.CharField(max_length=100)
    overview=models.TextField()
    release_date=models.DateField(null=True, blank=True)
    poster_path=models.TextField()
    vote_average=models.IntegerField()
    popularity=models.IntegerField()

    actors=models.ManyToManyField(Actor, related_name='movies')
    directors=models.ManyToManyField(Director, related_name='movies')
    genres=models.ManyToManyField(Genre, related_name='movies')


    # likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)


class Review(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_reviews')  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)

    # title, content, movie 응답받아서 넘겨줄 것, user는 request.user, likes는 비어있을 수 있음.

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,  related_name='ratings')
    score = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
