from django.shortcuts import render, redirect

from my_music_app.albums.forms import CreateAlbumForm, DeleteAlbumForm
from my_music_app.albums.models import Album


def create_album(request):
    form = CreateAlbumForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form,
    }
    return render(request, "albums/album-add.html", context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        "album": album,
    }
    return render(request, "albums/album-details.html", context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = CreateAlbumForm(request.POST or None, instance=album)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form,
        "album": album,
    }
    return render(request, "albums/album-edit.html", context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect("index")
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        "form": form,
        "album": album,
    }
    return render(request, "albums/album-delete.html", context)

