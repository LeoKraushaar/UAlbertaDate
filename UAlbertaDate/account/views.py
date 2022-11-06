from django.shortcuts import render, redirect
from .forms import PersonalInfoForm
from .models import UserInfo


BASE_URL = "http://127.0.0.1:8000/{}/"

# Create your views here.
def account(request):
    context = {}

    context["email"] = request.user.email
    context["chat_url"] = BASE_URL.format("chat")
    context["edit_info_url"] = BASE_URL.format("account/edit_info")
    return render(request, "account.html", context)

def edit_info(request):
    context = {}

    try:
        user_info = UserInfo.objects.get(user=request.user)
        initial = populate_form(user_info)
        form = PersonalInfoForm(request.POST, request.FILES, initial=initial)
    except:
        initial = {}

    if request.method == "POST":
        
        if not form.is_valid():
            context["errors"] = form.errors
        else:
            # Check if user already has info, if so, delete it before updating.
            try:
                UserInfo.objects.filter(user=request.user).delete()
            except:
                pass
            
            context["prints"] = form.cleaned_data
            new_info = form.save(commit=False)
            new_info.user = request.user
            new_info.first_name = request.user.first_name
            new_info.save()
            return redirect(BASE_URL.format("account"))
    
    elif request.method != "POST":
        form = PersonalInfoForm()
    
    context["form"] = form
    return render(request, "edit_info.html", context)

def populate_form(info):
    initial = {}
    for field_name in info._meta.get_all_field_names():
        try:
            initial[field_name] = getattr(info, field_name, None)
        except Exception as e:
            print(e)
    return initial

fields = [
            "height_ft",
            "looking_for",
            "major",
            "target_gender",
            "year_of_study",
            "most_hated_course",
            "age",
            "gender",
            "hometown",
            "bio"
]
