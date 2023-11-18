from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def preview_view(request):
    return render(request, template_name='preview.html')


# @login_required(redirect_field_name='preview')
def home(request):
    return render(request, template_name='home.html')


def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        send_mail(
            first_name,
            'Your Personality approved',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=loader.render_to_string('contact-us.html')
        )
        return redirect('contact-us')
    return render(request, template_name='contact-us.html')
