from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


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

def dashboard(request):
    return render(request, 'dashboard.html')
