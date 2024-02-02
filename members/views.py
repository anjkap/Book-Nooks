from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, UserProfileForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
#            return redirect('base')
            return HttpResponseRedirect('/userprofile/dashboard')
        else:
            messages.success(request, ("There was an error logging in, please try again."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were successfully logged out!"))
    return HttpResponseRedirect('/homepage/')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/members/user_profile')

    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {
        'form':form,
    })

def user_profile(request):
    submitted = False
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/userprofile/dashboard')
    else:
        form = UserProfileForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'authenticate/profile.html', {'form': form, 'submitted':submitted})