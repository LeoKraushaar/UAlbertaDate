from django.urls import path

from chat import views

urlpatterns = [
    path("chat/", views.all_chats),
    path("chat/<user_name>/", views.chat),
]