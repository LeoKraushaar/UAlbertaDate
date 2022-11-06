from django.urls import path

from chat import views

urlpatterns = [
    path("chat/", views.all_chats),
    path("chat/<str:room_url>/", views.chat),
]