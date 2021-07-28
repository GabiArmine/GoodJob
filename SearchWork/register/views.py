import sys
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from register.models import UserProfile

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

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('SearchWork:index')
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'SearchWork/profile_registration.html', context_dict)

class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'website': userprofile.website,
                                'picture': userprofile.picture})

        return (user, userprofile, form)
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)
        except TypeError:
            return redirect('rango:index')

        context_dict = {'userprofile': userprofile,
                        'selecteduser': user,
                        'form': form}
        return render(request, 'register/profile.html', context_dict)

@method_decorator(login_required)
def post(self, request, username):
    try:
        (user, userprofile, form) = self.get_user_details(username)
    except TypeError:
        return redirect('rango:index')
    form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
    if form.is_valid():
        form.save(commit=True)

        return redirect('rango:profile', user.username)
    else:
        print(form.errors)

    context_dict = {'userprofile': userprofile,
                    'selecteduser': user,
                    'form': form}
    return render(request, 'rango/profile.html', context_dict)