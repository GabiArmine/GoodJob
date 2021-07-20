from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register/registration.html', context=context)
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register/registration.html', context)
    return redirect("login")

def home(request):
   return render(request, 'register/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('register/profile.html'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'register/login.html')