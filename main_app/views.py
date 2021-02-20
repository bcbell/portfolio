from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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
    return render(request, 'project_page.html')

def experience(request):
    return render(request, 'experience_page.html')

def certifications(request):
    return render(request, 'certifications_page.html')

def connect(request):
    return render(request, 'connect_page.html' )

  
class BlogCreate(CreateView):
    model=Blog
    fields='__all__'
    success_url='/blog'
                                                     
class BlogUpdate(UpdateView):
    model=Blog
    fields='__all__'
    template_name='main_app/blog_form.html'
    success_url='/blog'
