from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms.photo import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = "photo/photo_list.html"
    context_object_name = "photo_list"
    paginate_by = 3
    ordering = ("-created_at",)

    # def get_queryset(self):
    #     posts = super().get_queryset()
    #     if self.request.user.is_authenticated and not self.request.user.has_perm("webapp.view_post"):
    #         posts = posts.filter(author__in=self.request.user.following.all())
    #     return posts


class PhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photo/photo_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photo/photo_update.html"
    permission_required = "webapp.change_photo"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photo/photo_delete.html"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})


class PhotoDetailView(DetailView):
    queryset = Photo.objects.all()
    template_name = "photo/photo_detail.html"

def photo_by_token(request, token):
    photo = get_object_or_404(Photo, access_token=token)
    return render(request, 'photo/photo_detail.html', {'photo': photo})
# class LikePhotoView(LoginRequiredMixin, View):
#
#     def get(self, request, *args, pk, **kwargs):
#         post = get_object_or_404(Photo, pk=pk)
#         if request.user in post.like_users.all():
#             post.like_users.remove(request.user)
#         else:
#             post.like_users.add(request.user)
#         return HttpResponseRedirect(self.request.GET.get("next", reverse("webapp:posts_list")))



