from django.shortcuts import render
from account.models import UserInfo
import random
# Create your views here.

def swipe(request):
    context = {}
    user = request.user
    user_info = UserInfo.objects.get(user=user)
    current_profile = None
    while not current_profile:
        available_infos = UserInfo.objects.all()
        try:
            profile = available_infos.order_by("?").first()
            if are_compatible(profile, user_info):
                current_profile = profile
                context["user_image"] = current_profile.image
        except:
            context["user_image"] = None
    
    user_info = UserInfo.objects.get(user=current_profile.user)
    context["profile_info"] = current_profile.get_attributes()
    
    return render(request, "swipe.html", context)

def are_compatible(info1, info2):
    try:
        assert info1.gender in info2.target_gender
        assert info2.gender in info1.target_gender
        return True
    
    except AssertionError:
        return False
