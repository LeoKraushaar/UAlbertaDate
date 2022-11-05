from django.shortcuts import render
import datetime

# Create your views here.
BASE_URL = "http://127.0.0.1:8000/"

def index(request):
    context = {}
    date = datetime.datetime.today()
    context["date"] = date
    context["login"] = BASE_URL + "login/"
    context["sign_up"] = BASE_URL + "signup/"
    return render(request, "index.html", context)
