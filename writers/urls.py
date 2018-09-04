from django.urls import path

from . import views

urlpatterns = [
    path('accounts/signup', views.SignupView.as_view(), name='writer-signup')
]