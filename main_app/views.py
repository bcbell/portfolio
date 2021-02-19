from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home_page.html')

def about(request):
    return render(request, 'about_page.html')

def blog(request):
    blogs=Blog.objects.all()
    return render(request, 'blog/blog_page.html', {"blogs": blogs})

def removeBlog(request, blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/blog')

def projects(request):
    return render(request, 'portfolio/project_page.html')

def experience(request):
    return render(request, 'portfolio/experience_page.html')

def certifications(request):
    return render(request, 'portfolio/certifications_page.html')

def connect(request):
    return render(request, 'connect/connect_page.html' )
    
class BlogCreate(CreateView):
    model=Blog
    fields='__all__'
    success_url='/blog'
                                                     
class BlogUpdate(UpdateView):
    model=Blog
    fields='__all__'
    template_name='main_app/blog_form.html'
    success_url='/blog'
