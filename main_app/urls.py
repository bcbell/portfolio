from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/create', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name='blog_update')
]
