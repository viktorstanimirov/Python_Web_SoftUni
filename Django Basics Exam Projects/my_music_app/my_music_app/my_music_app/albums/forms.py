from django import forms

from my_music_app.albums.models import Album


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

        widgets = {
            "album_name": forms.TextInput(
                attrs={
                    "placeholder": "Album Name",
                }
            ),
            "artist": forms.TextInput(
                attrs={
                    "placeholder": "Artist",
                }
            ),
            "genre": forms.Select(),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                }
            ),

            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "Image URL",
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "placeholder": "Price",
                }
            )
        }
