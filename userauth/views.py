from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account successfully created. Wait for admin approval to login.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = UserRegistrationForm()

    return render(request, 'userauth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data['email_or_username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email_or_username)  # Check by email
            except User.DoesNotExist:
                try:
                    user = User.objects.get(username=email_or_username)  # Check by username
                except User.DoesNotExist:
                    user = None

            if user and user.is_active:  # Check if user exists and is active
                user = authenticate(request, email=user.email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful!")
                    return redirect('posts:create_post')
                else:
                    messages.error(request, "Invalid password.")
            else:
                messages.error(request, "User not found or not activated.")
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = UserLoginForm()

    return render(request, 'userauth/login.html', {'form': form})


