import os

API_PORT = os.environ["API_PORT"]

TREZOR_URLS_BY_TOKENS = {
    "BTC": os.environ.get("TREZOR_URL_BTC", "https://btc2.trezor.io/api/v2/"),
    "ETH": os.environ.get("TREZOR_URL_ETH", "https://eth2.trezor.io/api/v2/"),
    "DOGE": os.environ.get("TREZOR_URL_DOGE", "https://doge2.trezor.io/api/v2/"),
    "BCH": os.environ.get("TREZOR_URL_BCH", "https://bch2.trezor.io/api/v2/"),
    "BTG": os.environ.get("TREZOR_URL_BTG", "https://btg2.trezor.io/api/v2/"),
}
