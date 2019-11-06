from django.urls import path
from .views import index, register, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='crud/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='crud/logout.html'), name='logout'),
    # after login urls
    path('dahboard/', dashboard, name='dashboard'),
]
