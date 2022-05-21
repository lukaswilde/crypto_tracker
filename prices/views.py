from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from prices.tasks import get_current_token_price


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    cardano_price = get_current_token_price("cardano")

    return render(request, "prices/index.html")
