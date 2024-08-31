from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name="photo",
        on_delete=models.SET_DEFAULT,
        default=1
    )
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.pk})