from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils.timezone import now
from .forms import UserRegistrationForm
from .models import Task, Reminder, DailyPlan
from datetime import date

@login_required
def today_plan(request):
    plan = DailyPlan.objects.filter(user=request.user, date=date.today()).first()
    return render(request, 'registration/today_plan.html', {'plan': plan})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'registration/task_list.html', {'tasks': tasks})

@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('reminder_time')
    return render(request, 'registration/reminder_list.html', {'reminders': reminders})

@staff_member_required
def logged_in_users_view(request):
    sessions = Session.objects.filter(expire_date__gte=now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid = data.get('_auth_user_id')
        if uid:
            uid_list.append(uid)
    users = User.objects.filter(id__in=uid_list)
    return render(request, 'registration/logged_in_users.html', {'users': users})

def logout_success(request):
    return render(request, 'registration/logout_success.html')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    reminders = Reminder.objects.filter(user=request.user).order_by('reminder_time')[:5]
    daily_plan = DailyPlan.objects.filter(user=request.user, date=date.today()).first()
    return render(request, 'registration/dashboard.html', {
        'tasks': tasks,
        'reminders': reminders,
        'daily_plan': daily_plan
    })

def redirect_to_register(request):
    return redirect('assistant:register')

def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('assistant:dashboard')
    return render(request, 'registration/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('assistant:logout_success')
