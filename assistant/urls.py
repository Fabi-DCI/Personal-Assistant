from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'assistant'

urlpatterns = [
    path('', views.redirect_to_register, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout-success/', views.logout_success, name='logout_success'),
    path('today-plan/', views.today_plan, name='today_plan'),
    path('tasks/', views.task_list, name='task_list'),
    path('reminders/', views.reminder_list, name='reminder_list'),
    path('admin/logged-in-users/', views.logged_in_users_view, name='logged_in_users'),
]
