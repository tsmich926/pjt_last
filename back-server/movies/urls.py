from django.urls import path
from movies import views


urlpatterns = [
    # movie whole
    path('movies/',views.movie_list),
    # movie detail
    path('movies/<int:movie_pk>/',views.movie_detail),
    # movie search & one movie not(detail)
    path('movies/search/<str:movie_title>/',views.movie_title_search_detail),
    # actor whole
    path('actors/',views.actor_list),
    # actor detail
    path('actors/<int:actor_pk>/',views.actor_detail),
    # director whole
    path('directors/',views.director_list),
    # director detail
    path('directors/<int:director_pk>/',views.director_detail),
    # genre whole
    path('genres/',views.genre_list),
    # genre detail
    path('genres/<int:genre_pk>/',views.genre_detail),

    # review whole
    path('reviews/',views.review_list),
    # review detail method에 따라 조회, 삭제, 수정
    path('reviews/<int:review_pk>/',views.review_detail),
    # review create
    path('movies/<int:movie_pk>/review/',views.create_review),

    # create comment
    path('movies/<int:review_pk>/comment/',views.create_comment),
    # comment method에 따라 조회, 삭제, 수정
    path('comments/<int:comment_pk>/',views.review_detail),
    
    # create rating
    path('movies/<int:movie_pk>/rating/',views.create_rating),
    # comment method에 따라 조회, 삭제, 수정
    path('ratings/<int:rating_pk>/',views.review_detail),


]