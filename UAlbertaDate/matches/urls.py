from django.urls import path
from account import views

urlpatterns = [
    path("matches/", views.account),
]