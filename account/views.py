from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def homepage(request):

    return render(request, 'account/index.html')


def register(request):

    form = CreateUserForm()
    if request.method == 'POST':

        form = CreateUserForm(data=request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")

    context = {'registerform': form}



    return render(request, 'account/register.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("profile")
    context = {'loginform': form}
    return render(request, 'account/my-login.html', context=context)


def dashboard(request):

    return render(request,'account/dashboard.html')


def profile_form(request):

    return render(request,'account/profile_form.html')


@login_required(login_url='my-login')
def profile(request):

    return render(request,'account/profile.html')

def user_logout(request):

    auth.logout(request)

    return redirect("")
