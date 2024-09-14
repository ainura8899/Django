from django.shortcuts import render
from . import models


def cloth_filter_view(request):
    if request.method == 'GET':
        cloth_children = models.Cloth.objects.filter(tags__name='для детей').order_by('-id')
        cloth_adults = models.Cloth.objects.filter(tags__name='для взрослых').order_by('-id')
        cloth_pensioners = models.Cloth.objects.filter(tags__name='для пенсионеров').order_by('-id')
        return render(
            request,
            template_name='filter_list.html',
            context={
                'cloth_children': cloth_children,
                'cloth_adults': cloth_adults,
                'cloth_pensioners': cloth_pensioners
            }
        )
