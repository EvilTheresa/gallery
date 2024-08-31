from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models import Photo
from ..models.favorites import PhotoLike


@method_decorator(csrf_exempt, name='dispatch')
class PostLikeToggle(View):
    def post(self, request, photo_id):
        photo = Photo.objects.get(id=photo_id)
        like, created = PhotoLike.objects.get_or_create(author=request.user, photo = photo)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({'liked': liked})
