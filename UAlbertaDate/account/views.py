from django.shortcuts import render, redirect
from .forms import PersonalInfoForm
from .models import UserInfo


BASE_URL = "http://127.0.0.1:8000/{}/"

# Create your views here.
def account(request):
    context = {}

    context["email"] = request.user.email
    context["matches_url"] = BASE_URL.format("matches")
    context["edit_info_url"] = BASE_URL.format("account/edit_info")
    return render(request, "account.html", context)

def edit_info(request):
    context = {}
    
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, request.FILES)
        if not form.is_valid():
            context["errors"] = form.errors
        else:
            # Check if user already has info, if so, delete it before updating.
            try:
                UserInfo.objects.filter(user=request.user).delete()
            except:
                pass

            new_info = form.save(commit=False)
            new_info.user = request.user
            new_info.save()
            return redirect(BASE_URL.format("account"))
    
    elif request.method != "POST":
        form = PersonalInfoForm()
    
    context["form"] = form
    return render(request, "edit_info.html", context)
