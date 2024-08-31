from django.contrib.auth import get_user_model
from django.db import models


class PhotoLike(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name="photo_likes",
        on_delete=models.SET_DEFAULT,
        default=1
    )
    photo = models.ForeignKey('webapp.photo', on_delete=models.CASCADE)