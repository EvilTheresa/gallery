from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms.album import AlbumForm
from webapp.models import Album


class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        original_qs = super().get_queryset()
        filtered_qs = original_qs.filter(Q(is_public=True) | Q(author=self.request.user))
        return filtered_qs

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(UpdateView, PermissionRequiredMixin):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_update.html'
    permission_required = "webapp.change_photo"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('album_list')
    template_name = 'albums/album_delete.html'
