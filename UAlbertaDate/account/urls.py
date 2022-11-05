from django.urls import path
from account import views

urlpatterns = [
    path("account/", views.account),
    path("account/edit_info/", views.edit_info),
]