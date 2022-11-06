from django.shortcuts import render, redirect
from .forms import PersonalInfoForm
from .models import UserInfo


BASE_URL = "http://127.0.0.1:8000/{}/"
INDEX_URL = "http://127.0.0.1:8000/index/"
SWIPE_URL = "http://127.0.0.1:8000/swipe/"
ACCOUNT_URL = "http://127.0.0.1:8000/account/"

# Create your views here.
def account(request):
    context = {}
    
    context["swipe_url"] = SWIPE_URL
    context["index"] = INDEX_URL
    context["email"] = request.user.email
    context["chat_url"] = BASE_URL.format("chat")
    context["edit_info_url"] = BASE_URL.format("account/edit_info")
    return render(request, "account.html", context)

def edit_info(request):
    context = {}
    context["index"] = INDEX_URL
    try:
        user_info = UserInfo.objects.get(user=request.user)
        form = PersonalInfoForm(instance=user_info)
    except:
        form = PersonalInfoForm()
        user_info = None

    if request.method == "POST":
        if user_info:
            form = PersonalInfoForm(request.POST, request.FILES, instance=user_info)
        else:
            form = PersonalInfoForm(request.POST, request.FILES)
        if not form.is_valid():
            context["errors"] = form.errors
        else:
            context["prints"] = form.cleaned_data
            new_info = form.save(commit=False)
            new_info.user = request.user
            new_info.first_name = request.user.first_name
            new_info.save()
            return redirect(BASE_URL.format("account"))
    
    context["account_url"] = ACCOUNT_URL
    context["swipe_url"] = SWIPE_URL
    context["form"] = form
    return render(request, "edit_info.html", context)
