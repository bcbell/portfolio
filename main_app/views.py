from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home_page.html')

def about(request):
    return render(request, 'about_page.html')

def blog(request):
    return render(request, 'blog_page.html')
  
class BlogCreate(CreateView):
    model=Blog
    fields='__all__'

class BlogUpdate(UpdateView):
    model=Blog
    fields='__all__'

