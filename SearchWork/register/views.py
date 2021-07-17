from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register/registration.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register/registration.html', context)

def home(request):
    return HttpResponse("bla bla bla")

def login(request):
    return render(request, 'register/login.html')