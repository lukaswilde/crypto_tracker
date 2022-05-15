from celery import shared_task
import requests


@shared_task
def get_current_token_price(token):
    parameters = {
        "ids": token,
        "vs_currencies": "eur",
        "include_market_cap": True,
        "include_24hr_vol": True,
        "include_last_updated": True,
    }

    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price", params=parameters
    )

    if response.status_code != 200:
        raise ValueError(
            f"Could not retrieve price for token {token},"
            f" status code {response.status_code} received"
        )

    return response.json()
