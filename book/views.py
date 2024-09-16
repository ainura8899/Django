from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from . import models, forms


# UPDATE
def book_list_edit_view(request):
    if request.method == "GET":
        # query запрос
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='crud/book_list_edit.html',
            context={
                'book_object': book_object
            }
        )

def update_book_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Новость отредактирована!!! <a href = "/book_list/">На список книг</a>')
    else:
        form = forms.BookForm(instance=book_id)

    return render(
        request,
        template_name= 'crud/update_book.html',
        context={
            'form': form,
            'book_id': book_id
        }
    )


# DELETE NEWS
def book_list_delete_view(request):
    if request.method == "GET":
        # query запрос
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='crud/book_list_delete.html',
            context={
                'book_object': book_object
            }
        )

def book_drop_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    book_id.delete()
    return HttpResponse('Книга удалена!!! <a href = "/book_list/">На список книг</a>')


# CREATE BOOKS

def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно отправлены!!! <a href = "/book_list/">На список книг</a>')
    else:
        form = forms.BookForm()
    return render(
        request,
        template_name='crud/create_book.html',
        context={
            'form': form
        }
    )


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
# вывод неполной информации
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
