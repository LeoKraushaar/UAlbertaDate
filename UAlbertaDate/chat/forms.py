from .models import Message, ChatRoom
from django.contrib.auth.models import User
from django import forms

class MessageForm(forms.ModelForm):

    index = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    user = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    chat_room = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )



    class Meta:
        model = Message
        fields = "__all__"