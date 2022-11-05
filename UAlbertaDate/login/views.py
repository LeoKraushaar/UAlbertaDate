from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

HOMEPAGE = "http://127.0.0.1:8000/index/"

# Create your views here.
def login(request):
    context = {"errors":[]}
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
    if form.is_valid():
         email = form.cleaned_data.get("username")
         password = form.cleaned_data.get("password")
         print(email, password)
         user = authenticate(username=email, password=password)
         if user:
            login(request, user)
            messages.info(request, "You are now logged in as {}.".format(email))
            return redirect(HOMEPAGE)
         else:
            context["errors"].append("Invalid username or password.")
    
    elif request.method != "POST":
        form = AuthenticationForm()

    context["form"] = form
    return render(request, "signin.html", context)