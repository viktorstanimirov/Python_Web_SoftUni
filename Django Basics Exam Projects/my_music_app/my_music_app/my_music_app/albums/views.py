from django.shortcuts import render, redirect

from my_music_app.albums.forms import CreateAlbumForm


def create_album(request):
    form = CreateAlbumForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form,
    }
    return render(request, "albums/album-add.html", context)

