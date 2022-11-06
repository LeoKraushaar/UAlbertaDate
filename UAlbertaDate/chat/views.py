from django.shortcuts import render
from swipe.models import LikeRelationship
from account.models import UserInfo
# Create your views here.

def all_chats(request):
    context = {}
    user = request.user
    liked_users = LikeRelationship.objects.filter(liker=user).all()
    likes_to_current_user = LikeRelationship.objects.filter(likee=user).all()
    matches = []
    for liked_user in liked_users:
        if liked_user in likes_to_current_user:
            matches.append(user)
    
    context["matches"] = matches
    return render(request, "all_chats.html", context)

def chat(request, user):
    context = {}

    return render(request, "chat.html", context)
