from django.shortcuts import render
from datetime import datetime
import time
from django.http import HttpResponse


# now = datetime.now().time()
# today = date. today()
def about_view(request):
    return HttpResponse("Меня зовут Айнура. Я обучаюсь Бэкенд в Geeks")

def my_friend_view(request):
    return HttpResponse("Моя подруга Асель. Она тоже хочет изучать Python")

def datetime_view(request):
    now = datetime.now()
    # return HttpResponse("Текущее время: ",now.strftime("%H:%M"))
    # return HttpResponse("Текущее время: ",isoformat())
    # return HttpResponse("Текущее время: ", today)
    formated_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"Текущее время:{formated_time}")



# Create your views here.
