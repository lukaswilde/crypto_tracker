from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/index.html")


def integrations(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/integrations.html")
