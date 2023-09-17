from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def registrationView(request):
    if request.method == "POST":
        # the files is because we have image
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            #user = form.save will log in the user directly instead of after user has registered she or he will still do login
            user = form.save()

            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    context = {"form":form}

    return render (request, "user/register.html", context)

def loginUser(request):
    if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         user = authenticate(request, username=username, password=password)

         if user is not None:
             login(request, user)
             return redirect("home")
         else:
            messages.error(request, "invalid user or password")

    return render (request, "user/login-user.html")

def logoutUser(request):
    logout(request)
    return redirect ("login-user")
