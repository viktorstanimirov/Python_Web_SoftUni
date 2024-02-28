from django.shortcuts import render


def create_album(request):
    return render(request, "albums/add-album.html")
