from rest_framework import serializers
from .models import Movie,Actor,Director,Genre,Review,Rating,Comment
from django.conf import settings
from accounts.serializers import UserSerializer

# 주의사항
# 참조키가 모델에 있는 경우 readonly로 바꾼 다음 serializer.save('title'=title)와 같이 사용해야 함
# manytomanyfiled는 


# base

# movies/
# 영화 전체 목록
# movies/search/<str:movie_title>/
# 영화 검색 시 보내줄 데이터
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=('movie','user')
        # 참조키, movie, user user==request.user로 받아도 됨.

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        read_only_fields=('review','user')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'
        read_only_fields=('movie','user')






# movies/<int:movie_pk>/
# 영화 디테일
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
        # read_only_fields=('actors_settt',)
    actors=ActorSerializer(many=True,read_only=True)
    directors=DirectorSerializer(many=True,read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)
    review_count=serializers.IntegerField(source='reviews.count',read_only=True)

# actors/<int:actor_pk>/
# 배우 디테일
class ActorDetailSerializer(serializers.ModelSerializer):
    movies=MovieSerializer(many=True,read_only=True)
    like_users=UserSerializer(many=True, read_only=True)
    class Meta:
        model=Actor
        fields='__all__'

# directors/<int:director_pk>/
# 감독 디테일
class DirectorDetailSerializer(serializers.ModelSerializer):
    movies=MovieSerializer(many=True,read_only=True)
    like_users=UserSerializer(many=True, read_only=True)
    class Meta:
        model=Director
        fields='__all__'

# genres/<int:genre_pk>/
# 장르 디테일
class GenreDetailSerializer(serializers.ModelSerializer):
    movies=MovieSerializer(many=True, read_only=True)
    like_users=UserSerializer(many=True, read_only=True)
    class Meta:
        model=Director
        fields='__all__'

# 리뷰 디테일
class ReviewDetailSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True, read_only=True)
    like_users=UserSerializer(many=True, read_only=True)
    class Meta:
        model=Review
        fields='__all__'







# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Review
#         fields='__all__'
#         read_only_fields=('movie',)





## movies/search/<str:movie_title>/
## 영화 검색 시 보내줄 데이터
class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
        # read_only_fields=('actors_settt',)