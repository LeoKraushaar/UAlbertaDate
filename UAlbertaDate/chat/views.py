from django.shortcuts import render
from swipe.models import LikeRelationship
from account.models import UserInfo
# Create your views here.

def all_chats(request):
    context = {}
    user = request.user
    likes = LikeRelationship.objects.filter(liker=user)

    return render(request, "all_chats.html", context)

def chat(request, user):
    context = {}

    return render(request, "chat.html", context)
