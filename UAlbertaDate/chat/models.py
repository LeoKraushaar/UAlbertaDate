from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatRoom(models.Model):
    user_one = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    user_two = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name = "+"
    )

    url = models.CharField(
        max_length=40
    )


class Message(models.Model):

    text = models.CharField(
        max_length=200
        )

    chat_room = models.ForeignKey(
        to=ChatRoom,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    message_index = models.IntegerField(
        blank=True,
        null=True,
    )

