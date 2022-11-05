from django.urls import path
from account import views

urlpatterns = [
    path("account/", views.account),
    path("acccount/my_info", views.my_info),
]