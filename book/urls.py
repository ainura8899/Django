from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view, name='book_list'),

    path('book_list_delete/', views.book_list_delete_view, name='book_list_delete'),
    path('book_list/<int:id>/delete/', views.book_drop_view),
    path('book_list_edit/', views.book_list_edit_view, name='book_list_edit'),
    path('book_list/<int:id>/update/', views.update_book_view),


    path('book_list/<int:id>/', views.book_detail_view),
    path('create_book/', views.create_book_view, name='add_books'),

    path('about_me/', views.about_view),
    path('my_friend/', views.my_friend_view),
    path('datetime/', views.datetime_view),
]

