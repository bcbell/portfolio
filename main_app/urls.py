from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Blog Page

    path('blog/', views.blog, name='blog'),
    # path('blog/<int:blog_id>', views.BlogDetail.as_view(), name='blog_detail'),
    path('blog/create', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<int:blog_id>/delete', views.removeBlog, name='blog_delete'),
    
    # Project Page
    path('portfolio/projects/', views.projects, name='projects'),
    path('portfolio/experience/', views.experience, name='experience'),
    path('portfolio/certifications/', views.certifications, name='certifications'),

    #Connect Page
    path('connect/', views.connect, name='connect'),
]
