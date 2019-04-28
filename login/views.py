from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request):
return render(request,'YAB/login.html')
