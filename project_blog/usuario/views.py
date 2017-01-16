from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from usuario.forms import RegistroForm
from usuario.forms import LoginFrom
# Create your views here.


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('blog_apps:post_list')


class LoginUsuario(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginFrom
    success_url = reverse_lazy('blog_apps:post_list')


class Forgotpass(TemplateView):
    template_name = 'usuario/forgotpass.html'
