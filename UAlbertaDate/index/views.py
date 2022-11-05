from django.shortcuts import render
import datetime

# Create your views here.
BASE_URL = "http://127.0.0.1:8000/"

def index(request):
   context = {"account_url":BASE_URL + "account/"}
   return None
