from django.contrib.auth import get_user_model
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name="album",
        on_delete=models.SET_DEFAULT,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
