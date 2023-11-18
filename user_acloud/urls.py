from django.urls import path
from .views import signupview

urlpatterns = [
    path('sign-up/', signupview, name='sign-up')
]
