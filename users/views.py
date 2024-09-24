from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models,  middlewares


class RegistrationView(CreateView):
    # form_class = UserCreationForm
    form_class = forms.CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        level = form.cleaned_data['level']
        if level == 'junior':
            self.object.salary = 500
        elif level == 'middle':
            self.object.salary = 1000
        elif level == 'senior':
            self.object.salary = 3000
        else:
            self.object.salary = 0
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salary'] = getattr(self.request, 'salary', "Зарплата не определена")
        return context
