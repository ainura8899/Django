from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_view),
    path('my_friend/', views.my_friend_view),
    path('datetime/', views.datetime_view),
]

