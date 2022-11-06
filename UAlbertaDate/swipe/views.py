from django.shortcuts import render, redirect
from account.models import UserInfo
from .forms import LikeForm
from .models import LikeRelationship
from django.contrib.auth.models import User
# Create your views here.

STATIC_URL = "http://127.0.0.1:8000/static/media/{}"
SWIPE_URL = "http://127.0.0.1:8000/swipe/"

def swipe(request):
    context = {}
    user = request.user
    user_info = UserInfo.objects.get(user=user)
    current_profile = None
    while not current_profile:
        available_infos = UserInfo.objects.all()
        try:
            profile = available_infos.order_by("?").first()
            if are_compatible(profile, user_info) and is_viable(profile, user_info):
                current_profile = profile
        except:
            context["user_image"] = None
    user_info = UserInfo.objects.get(user=current_profile.user)

    if request.method == "POST":
        like_form = LikeForm(request.POST)
        if like_form.is_valid():
            like_relationship = LikeRelationship(liker=user, likee=current_profile.user)
            if not LikeRelationship.objects.filter(liker=user, likee=current_profile.user).exists():
                like_relationship.save()
        else:
            return redirect(SWIPE_URL)

    
    context["first_name"] = current_profile.user.first_name
    context["profile_info"] = current_profile.get_attributes()
    context["image_url"] = STATIC_URL.format(current_profile.image_file)
    return render(request, "swipe.html", context)

def are_compatible(info1, info2):
    try:
        assert info1.gender in info2.target_gender
        assert info2.gender in info1.target_gender
        return True
    
    except AssertionError:
        return False

def is_viable(profile, user_info):
    try:
        assert profile.user != user_info.user
        assert not LikeRelationship.objects.get(liker=user_info.user, likee=profile.user)
        return True
    except AssertionError:
        return False