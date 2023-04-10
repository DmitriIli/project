from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignupForm


class BaseRegisterView(CreateView):
    model = User
    form_class = SignupForm
    success_url = '/sign/login/'

