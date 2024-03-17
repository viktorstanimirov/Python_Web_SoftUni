from django.shortcuts import render


def catalog(request):
    return render(request, "plants/catalogue.html")
