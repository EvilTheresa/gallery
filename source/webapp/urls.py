from django.urls import path

from webapp.views.album import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
from webapp.views.photo import PhotoListView, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView

app_name = "webapp"

urlpatterns = [
    path('', PhotoListView.as_view(), name="photo_list"),
    path('posts/add/', PhotoCreateView.as_view(), name="photo_add"),
    path('post/<int:pk>/', PhotoDetailView.as_view(), name="photo_view"),
    path('post/<int:pk>/update/', PhotoUpdateView.as_view(), name="photo_update"),
    path('post/<int:pk>/delete/', PhotoDeleteView.as_view(), name="photo_delete"),
    # path('post/<int:pk>/like/', LikePostView.as_view(), name="post_like"),
    # path('api/post/<int:post_id>/toggle_like/', PostLikeToggle.as_view(), name='article_like_toggle'),

    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album_view'),
    path('albums/new/', AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_update'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
