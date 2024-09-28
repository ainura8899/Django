from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from . import models, forms

# CREATE MOVIES
class MovieCreateView(generic.CreateView):
    template_name = 'crud/create_movie.html'
    form_class = forms.MovieForm
    success_url = '/movie_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MovieCreateView, self).form_valid(form=form)

# вывод неполной информации
class MovieListView(generic.ListView):
    template_name = 'movie_list.html'
    context_object_name = 'movie_object'
    model = models.Movie

    def get_queryset(self): # создаем query запрос
        return self.model.objects.all().prefetch_related('review_movie').all().order_by('-id')


# для полной информации
class MovieDetailView(generic.DetailView):
    template_name = 'movie_detail.html'
    context_object_name = 'movie_id'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)

# DELETE NEWS
class MovieListDeleteView(generic.ListView):
    template_name = 'crud/movie_list_delete.html'
    context_object_name = 'movie_object'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class MovieDropDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/movie_list_delete/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)

# UPDATE
class MovieUpdateListView(generic.ListView):
    template_name = 'crud/movie_list_edit.html'
    context_object_name = 'movie_object'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class MovieEditView(generic.UpdateView):
    template_name = 'crud/update_movie.html'
    form_class = forms.MovieForm
    success_url = '/movie_list_edit/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)