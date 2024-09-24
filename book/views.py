from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from . import models, forms

class SearchView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_object'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

# вывод неполной информации
class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self): # создаем query запрос
        return self.model.objects.all().prefetch_related('review_book').all().order_by('-id')


# # def book_list_view(request):
# #     if request.method == "GET":
# #         # query запрос
# #         book_object = models.Book.objects.all()
# #         return render(
# #             request,
# #             template_name='book_list.html',
# #             context={
# #                 'book_object': book_object
# #             }
# #         )

# для полной информации
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Book, id=id)
#         return render(
#             request,
#             template_name='book_detail.html',
#             context={
#                 'book_id': book_id
#             }
#         )


# CREATE BOOKS

class BookCreateView(generic.CreateView):
    template_name = 'crud/create_book.html'
    form_class = forms.BookForm
    success_url = '/book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Данные успешно отправлены!!! <a href = "/book_list/">На список книг</a>')
#     else:
#         form = forms.BookForm()
#     return render(
#         request,
#         template_name='crud/create_book.html',
#         context={
#             'form': form
#         }
#     )


# DELETE NEWS
class BookListDeleteView(generic.ListView):
    template_name = 'crud/book_list_delete.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class BookDropDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/book_list_delete/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


# def book_list_delete_view(request):
#     if request.method == "GET":
#         # query запрос
#         book_object = models.Book.objects.all()
#         return render(
#             request,
#             template_name='crud/book_list_delete.html',
#             context={
#                 'book_object': book_object
#             }
#         )

# def book_drop_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     return HttpResponse('Книга удалена!!! <a href = "/book_list/">На список книг</a>')

# UPDATE
class BookUpdateListView(generic.ListView):
    template_name = 'crud/book_list_edit.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class BookEditView(generic.UpdateView):
    template_name = 'crud/update_book.html'
    form_class = forms.BookForm
    success_url = '/book_list_edit/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)



# def book_list_edit_view(request):
#     if request.method == "GET":
#         # query запрос
#         book_object = models.Book.objects.all()
#         return render(
#             request,
#             template_name='crud/book_list_edit.html',
#             context={
#                 'book_object': book_object
#             }
#         )

# def update_book_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Новость отредактирована!!! <a href = "/book_list/">На список книг</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#
#     return render(
#         request,
#         template_name= 'crud/update_book.html',
#         context={
#             'form': form,
#             'book_id': book_id
#         }
#     )












def about_view(request):
    return HttpResponse("Меня зовут Айнура. Я обучаюсь Бэкенд в Geeks")

def my_friend_view(request):
    return HttpResponse("Моя подруга Асель. Она тоже хочет изучать Python")

def datetime_view(request):
    now = datetime.now()
    formated_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"Текущее время:{formated_time}")



# Create your views here.
