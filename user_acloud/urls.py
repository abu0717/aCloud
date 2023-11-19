from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('sign-up/', signup_view, name='sign-up'),
    path('login/', login_view, name='login'),
    path('log-out/', logout_view, name='logout')
]
