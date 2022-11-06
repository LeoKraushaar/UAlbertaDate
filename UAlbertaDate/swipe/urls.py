from django.urls import path
from swipe import views

urlpatterns = [
    path("swipe/", views.swipe),
    ]