from django.shortcuts import render
from django.http import HttpResponse
from .tasks import get_current_token_price
import json

# Create your views here.
def index(request):
    cardano_price = get_current_token_price("cardano")

    return HttpResponse(round(cardano_price["cardano"]["eur"], 2))
