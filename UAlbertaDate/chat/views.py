from django.shortcuts import render, redirect
from swipe.models import LikeRelationship
from account.models import UserInfo
from .models import ChatRoom, Message
from .forms import MessageForm
from django.contrib.auth.models import User
# Create your views here.

CHAT_URL = "http://127.0.0.1:8000/chat/"
INDEX_URL = "http://127.0.0.1:8000/index/"
ACCOUNT_URL = "http://127.0.0.1:8000/account/"

def all_chats(request):
    context = {}
    context["index"] = INDEX_URL
    user = request.user
    matched_profiles = matches(user)
    match_urls = image_urls(matched_profiles)
    links = chat_links(user, matched_profiles)

    context["account_url"] = ACCOUNT_URL
    context["match_set"] = set(zip(matched_profiles, match_urls, links))
    return render(request, "all_chats.html", context)

def chat(request, room_url:str):
    context = {}
    context["index"] = INDEX_URL
    try:
        room = ChatRoom.objects.get(url=room_url)
    except:
        ccids = ccids_from_url(room_url)
        users = users_from_ccids(ccids)
        room = ChatRoom.objects.create(user_one=users[0], user_two=users[1], url=room_url)

    if request.method == "POST":
        new_message = MessageForm(request.POST)
        if new_message.is_valid():
            new_message = new_message.save(commit=False)
            new_message.chat_room = room
            new_message.message_index = get_num_messages(room) + 1
            new_message.user = request.user
            new_message.save()
            return redirect(CHAT_URL + room_url)
   
    elif request.method != "POST":
        new_message = MessageForm()

    context["all_chats_url"] = CHAT_URL
    context["form"] = new_message
    context["messages"] = Message.objects.filter(chat_room=room)
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

def users_from_ccids(ccids):
    user_one = User.objects.get(email=ccids[0]+"@ualberta.ca")
    user_two = User.objects.get(email=ccids[1]+"@ualberta.ca")
    return (user_one, user_two)

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

def chat_links(user, matches):
    ccids = []
    for match in matches:
        chat_link = get_chat_url(user, match)
        ccids.append(CHAT_URL + chat_link + "/")
    
    return ccids

def get_chat_url(user_one, user_two):
    sorted_names = sorted([get_ccid(user_one), get_ccid(user_two)])
    chat_href = "-".join(sorted_names)
    return chat_href

def ccids_from_url(url):
    return url.split("-")

def get_num_messages(room):
    messages = Message.objects.filter(chat_room=room).all()
    return len(messages)