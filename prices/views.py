from django.http import HttpResponse, HttpRequest

from .tasks import get_current_token_price


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    cardano_price = get_current_token_price("cardano")

    return HttpResponse(round(cardano_price["cardano"]["eur"], 2))
