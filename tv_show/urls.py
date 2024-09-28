from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),

    path('movie_list_delete/', views.MovieListDeleteView.as_view(), name='movie_list_delete'),
    path('movie_list/<int:id>/delete/', views.MovieDropDeleteView.as_view()),
    path('movie_list_edit/', views.MovieUpdateListView.as_view(), name='movie_list_edit'),
    path('movie_list/<int:id>/update/', views.MovieEditView.as_view()),


    path('movie_list/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('create_movie/', views.MovieCreateView.as_view(), name='add_movie'),

    ]