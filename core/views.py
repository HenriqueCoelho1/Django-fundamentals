from django.shortcuts import render


def index(request):
    data = {"movie": "a good data"}
    return render(request, "index.html", data)


def contact(request):
    return render(request, "contact.html")
