from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(),
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')