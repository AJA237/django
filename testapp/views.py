from django.shortcuts import render, HttpResponse
# from django.view.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from .models import UserModel
from .form import UserForm

# Create your views here.
# class HomeView(TemplateView):
#     template_name = '/home'
    
# class InfoCreateView(CreateView):
#     model = UserModel
#     template_name =  "info.html"
#     form_class = UserForm
#     success_url = '/home/'

# class InfoListView(ListView):
#     model = UserModel
#     template_name = "home.html"
    
# class InfoUpdateView(UpdateView):
#     model = UserModel
#     template_name = "info.html"
#     form_class = UserForm
#     success_url = '/home/'

def save_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        user = UserModel(first_name=first_name, last_name=last_name, age=age, email=email)
        user.save()

        return HttpResponse('User saved successfully!')
    else:
        return HttpResponse('Invalid request method')