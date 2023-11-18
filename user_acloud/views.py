from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm


# Create your views here.

def signupview(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    return render(request, template_name='sign-up.html', context=
    {
        "form": form
    })


def loginview(request):
    return render(request, template_name='login.html')


def logout_view(request):
    ...
