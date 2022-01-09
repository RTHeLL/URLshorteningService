from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import NoReverseMatch, reverse_lazy
from django.views.generic import CreateView

from .database.controller import URLController
from .forms import URLGenerateForm, UserRegisterForm, UserLoginForm

url_controller = URLController()


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self) -> '302':
        return reverse_lazy('home')


def index(request: 'django_reqeust') -> 'html':
    if request.method == 'POST':
        form = URLGenerateForm(request.POST)
        if form.is_valid():
            shorted_url = url_controller.get_or_create_url(full_url=form.cleaned_data['full_url'],
                                                           author_id=request.user.pk)
            messages.success(request, request.build_absolute_uri(shorted_url))
    else:
        form = URLGenerateForm()
    return render(request, 'main/generate.html', {'form': form})


@login_required(login_url='login')
def urls_list(request: 'django_reqeust') -> 'html':
    urls = url_controller.get_urls_by_user_pk(request.user.pk)
    return render(request, 'main/urls.html', {'urls': urls})


def redirect_original(request: 'django_reqeust', url_slug: 'slug') -> '302':
    to_url = url_controller.get_full_url(url_slug=url_slug)
    try:
        return redirect(to_url)
    except NoReverseMatch:
        raise Http404()


def do_logout(request: 'django_reqeust') -> '302':
    logout(request)
    return redirect('login')


def page_not_found(request: 'django_reqeust', exception: Exception) -> 'html':
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
