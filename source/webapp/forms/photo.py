from django import forms

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    album = forms.ModelChoiceField(
        queryset=Album.objects.all(),
        required=False,
        label='Альбом',
        empty_label="Без альбома"
    )

    class Meta:
        model = Photo
        fields = ["image", "caption", "album"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['album'].queryset = Album.objects.filter(author=user)
