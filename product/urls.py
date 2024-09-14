from django.urls import path
from . import views

urlpatterns = [
    path('cloth_children/', views.cloth_filter_view),
    path('cloth_adults/', views.cloth_filter_view),
    path('cloth_pensioners/', views.cloth_filter_view),
]