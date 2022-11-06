from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

INDEX_URL = "http://127.0.0.1:8000/index/"

def verify_email(email):
    try:
        at_idx = email.index("@")
    except ValueError:
        raise ValidationError(message="please enter a valid email address.")
    if not email[at_idx+1:] == "ualberta.ca":
        raise ValidationError(message="Please enter a ualberta email.")
    if not email[:at_idx].isalpha():
        raise ValidationError(message="please enter a valid email address.")

# Create your views here.
def signup(request):
    context = {"errors":[]}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            first_name = form.cleaned_data.get("first_name")
            if User.objects.filter(email=email).exists():
                context["errors"].append("an account already exists with this email address.")
                form = SignUpForm()
            else:
                user_instance = User.objects.create_user(
                    username=email, 
                    email=email, 
                    password=password,
                    first_name=first_name
                )
                user_instance.save()
                return redirect("http://127.0.0.1:8000/index/")

    elif request.method != "POST":
        form = SignUpForm()
    
    context["index"] = INDEX_URL
    context["form"] = form
    return render(request, "signup.html", context)