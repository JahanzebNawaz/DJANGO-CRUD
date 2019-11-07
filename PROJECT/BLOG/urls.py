from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog'),
    path('blogpost/<int:blog_id>', views.blogpost, name='blogpost'),
    path('bloglist/<int:author_id>', views.bloglist, name='bloglist'),
    path('blogpublish/', views.blogpublish, name='blogpublish'),
    path('blogupdate/<int:id>', views.blogupdate, name='blogupdate'),
    path('blogdelete/<int:id>', views.blogdelete, name='blogdelete'),
]

