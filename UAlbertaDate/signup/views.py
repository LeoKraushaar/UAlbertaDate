from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError

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
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            if User.objects.filter(email=email).exists():
                messages.error("an account already exists with this email address.")
                form = SignUpForm()
            else:
                user_instance = User.objects.create_user(
                    username=email, 
                    email=email, 
                    password=password
                )
                user_instance.save()

    
    elif request.method != "POST":
        form = SignUpForm()
    
    return request(request, "signup", context)