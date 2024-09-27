from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),

    path('book_list_delete/', views.BookListDeleteView.as_view(), name='book_list_delete'),
    path('book_list/<int:id>/delete/', views.BookDropDeleteView.as_view()),
    path('book_list_edit/', views.BookUpdateListView.as_view(), name='book_list_edit'),
    path('book_list/<int:id>/update/', views.BookEditView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),


    path('book_list/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create_book/', views.BookCreateView.as_view(), name='add_books'),

    path('about_me/', views.about_view),
    path('my_friend/', views.my_friend_view),
    path('datetime/', views.datetime_view),
]

