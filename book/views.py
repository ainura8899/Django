from django.shortcuts import render, get_object_or_404
from datetime import datetime
import time
from django.http import HttpResponse
from . import models

# для полной информации
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id
            }
        )
# вывод не полной информации
def book_list_view(request):
    if request.method == "GET":
        # query запрос
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'book_object': book_object
            }
        )


def about_view(request):
    return HttpResponse("Меня зовут Айнура. Я обучаюсь Бэкенд в Geeks")

def my_friend_view(request):
    return HttpResponse("Моя подруга Асель. Она тоже хочет изучать Python")

def datetime_view(request):
    now = datetime.now()
    formated_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"Текущее время:{formated_time}")



# Create your views here.
