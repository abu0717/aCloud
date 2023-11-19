from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _, get_language, activate


# Create your views here.


def preview_view(request):
    trans = translate(language='uz')
    return render(request, template_name='preview.html', context={
        'trans': trans
    })


def translate(language):
    current_language = get_language()
    try:
        activate(language)
        text = _("hello")
    finally:
        activate(current_language)
    return text


@login_required
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
            html_message=loader.render_to_string('email.html', context={
                'first_name': first_name,
                'last_name': last_name
            })
        )
        return redirect('contact-us')
    return render(request, template_name='contact-us.html')
