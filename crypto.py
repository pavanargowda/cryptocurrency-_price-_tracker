import requests

API_URL = "https://api.coingecko.com/api/v3/coins/markets"


def get_crypto_prices():

    parameters = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    try:
        response = requests.get(
            API_URL,
            params=parameters,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.RequestException as error:
        print("Error fetching cryptocurrency prices:", error)
        return None
