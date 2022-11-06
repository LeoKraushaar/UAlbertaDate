from django.shortcuts import render, redirect
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from account.models import UserInfo

HOMEPAGE = "http://127.0.0.1:8000/index/"
ACCOUNT_URL = "http://127.0.0.1:8000/account/"
SWIPE_URL = "http://127.0.0.1:8000/swipe/"
INDEX_URL = "http://127.0.0.1:8000/index/"

# Create your views here.
def login(request):
    context = {"errors":[]}
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user:
                lg(request=request, user=user)
                if UserInfo.objects.filter(user=request.user):
                    return redirect(SWIPE_URL)
                else:
                    return redirect(ACCOUNT_URL)
            else:
                context["errors"].append("Invalid username or password.")
                form = AuthenticationForm()
    
    elif request.method != "POST":
        form = AuthenticationForm()

    context["index"] = INDEX_URL
    context["form"] = form
    return render(request, "login.html", context)