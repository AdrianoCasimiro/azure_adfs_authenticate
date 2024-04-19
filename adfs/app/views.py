from django.shortcuts import render
from django.http import HttpResponse


def login_successful(request):
    return HttpResponse('Login successful!')
