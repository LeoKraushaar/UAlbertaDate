from django.urls import path

from chat import views

urlpatterns = [
    path("chat/", views.all_chats),
    path("chat/<str:user>/", views.chat),
]