from django.urls import path
from .views import home, signupview, loginview, preview_view, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('sign-up/', signupview, name='sign-up'),
    path('login/', loginview, name='login'),
    path('preview/', preview_view, name='preview'),
    path('contact-us/', contact_view, name='contact-us')
]