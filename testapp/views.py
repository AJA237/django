from django.shortcuts import render
from django.view.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from .models import UserModel
from .form import UserForm

# Create your views here.
class HomeView(TemplateView):
    template_name = '/home'
    
class InfoCreateView(CreateView):
    model = UserModel
    template_name =  "info.html"
    form_class = UserForm
    success_url = '/home/'

class InfoListView(ListView):
    model = UserModel
    template_name = "home.html"
    
class InfoUpdateView(UpdateView):
    model = UserModel
    template_name = "info.html"
    form_class = UserForm
    success_url = '/home/'