from django.shortcuts import render, redirect
from .forms import RegisterVendorForm, RegisterRiderForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .decorators import unauthenticated_user


def register_vendor(request):
    form = RegisterVendorForm
    if request.method == 'POST':
        form = RegisterVendorForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='vendor')
            user.groups.add(group)
            messages.success(request, username + " is registered as vendor.")
            return redirect('create_vendor')
    context = {'form': form}
    template = 'account/register_vendor.html'
    return render(request, template, context)


def register_rider(request):
    form = RegisterRiderForm
    if request.method == 'POST':
        form = RegisterRiderForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='rider')
            user.groups.add(group)
            messages.success(request, username + " is registered as rider.")
            return redirect('create_rider')
    context = {'form': form}
    template = 'account/register_rider.html'
    return render(request, template, context)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect username or password')
    context = {}
    template = 'account/login.html'
    return render(request, template, context)


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    context = {}
    template = 'account/home.html'
    return render(request, template, context)
