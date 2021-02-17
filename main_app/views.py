from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

def about(request):
    return render(request, 'about_page.html')

def blog(request):
    return render(request, 'blog_page.html')
    