from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LikeRelationship(models.Model):

    liker = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT
    )
    likee = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name = "+"
    )