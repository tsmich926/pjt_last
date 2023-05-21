from rest_framework import serializers
# from .models import Movie,Actor,Director,Genre,Review,Ratings,Comment
# from django.conf import settings
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  get_user_model()
        fields = '__all__'