from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    # path('blog/<int:blog_id>', views.BlogDetail.as_view(), name='blog_detail'),
    path('blog/create', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<int:blog_id>/delete', views.removeBlog, name='blog_delete'),
]
