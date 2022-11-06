from django.shortcuts import render
from swipe.models import LikeRelationship
from account.models import UserInfo
# Create your views here.

CHAT_URL = "http://127.0.0.1:8000/chat/"

def all_chats(request):
    context = {}
    user = request.user
    matched_profiles = matches(user)
    match_urls = image_urls(matched_profiles)
    
    ccid = get_ccid(user)
    context["link_to_chat"] = CHAT_URL + ccid + "/"

    context["match_dict"] = dict(zip(matched_profiles, match_urls))
    return render(request, "all_chats.html", context)

def chat(request, user):
    context = {}
    
    return render(request, "chat.html", context)

def matches(user):
    liked_users = LikeRelationship.objects.filter(liker=user).all()
    likes_to_current_user = LikeRelationship.objects.filter(likee=user).all()
    users_who_liked_current_user = [obj.liker for obj in likes_to_current_user]
    matches = []
    for liked_user in liked_users:
        if liked_user.likee in users_who_liked_current_user:
            matches.append(liked_user.likee)
    return matches

def image_urls(matches):
    urls = []
    for user in matches:
        user_info = UserInfo.objects.get(user=user)
        urls.append(user_info.get_image_url())
    return urls

def get_ccid(user):
    at_index = user.email.index("@")
    ccid = user.email[:at_index]
    return ccid