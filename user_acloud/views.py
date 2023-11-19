from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


# Create your views here.

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    return render(request, template_name='sign-up.html', context=
    {
        "form": form
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username is not None:
            login(request, user)
            return redirect('home')
        else:
            raise ValidationError('Invalid username or password.')
    return render(request, template_name='login.html', context={
    })


def logout_view(request):
    logout(request)
    return redirect('login')
