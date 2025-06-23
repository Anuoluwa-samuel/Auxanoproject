from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html' {'form': form} )

def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')