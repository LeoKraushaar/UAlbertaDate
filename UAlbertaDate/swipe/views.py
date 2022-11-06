from django.shortcuts import render
from account.models import UserInfo
# Create your views here.

STATIC_URL = "http://127.0.0.1:8000/static/media/{}"

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
        except:
            context["user_image"] = None
    
    user_info = UserInfo.objects.get(user=current_profile.user)
    context["profile_info"] = current_profile.get_attributes()
    
    context["image_url"] = STATIC_URL.format(current_profile.image_file)
    context["prints"] = STATIC_URL.format(current_profile.image_file)
    return render(request, "swipe.html", context)

def are_compatible(info1, info2):
    try:
        assert info1.gender in info2.target_gender
        assert info2.gender in info1.target_gender
        return True
    
    except AssertionError:
        return False
