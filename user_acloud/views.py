from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def signupview(request):
    return render(request, template_name='sign-up.html')


def loginview(request):
    return render(request, template_name='login.html')

