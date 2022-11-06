from .models import Message, ChatRoom
from django.contrib.auth.models import User
from django import forms

class MessageForm(forms.ModelForm):

    message_index = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            'user':forms.HiddenInput(),
            "chat_room":forms.HiddenInput()
        }