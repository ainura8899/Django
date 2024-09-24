from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ProgrammerLevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            level = str(request.POST.get('level'))
            if level == 'junior':
                request.salary = 500
            elif level == 'middle':
                request.salary = 1000
            elif level == 'senior':
                request.salary = 3000
            else:
                return HttpResponseBadRequest('Введите верный уровень: junior/ middle/ senior')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Зарплата не определена')

