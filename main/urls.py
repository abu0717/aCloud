from django.urls import path
from .views import home, preview_view, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('preview/', preview_view, name='preview'),
    path('contact-us/', contact_view, name='contact-us')
]