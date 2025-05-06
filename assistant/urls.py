from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'assistant'

urlpatterns = [
    path('', views.redirect_to_register, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='assistant:login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]