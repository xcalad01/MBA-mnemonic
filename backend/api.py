from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from backend.settings import TREZOR_URLS_BY_TOKENS, API_PORT

import requests
from requests.adapters import HTTPAdapter, Retry


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])

CHECK_ADDRESS_SESSION = requests.Session()
CHECK_ADDRESS_SESSION.mount('https://', HTTPAdapter(max_retries=retries))

TRANSACTIONS_INFO_SESSION = requests.Session()
TRANSACTIONS_INFO_SESSION.mount('https://', HTTPAdapter(max_retries=retries))

@app.route("/ping")
def ping():
    return jsonify({"pong": True})


@app.route("/transaction_specific", methods=["POST"])
def transaction_info():
    r = request.get_json()
    token = r.get("token")
    if not token:
        return jsonify({"message": "token not specified"})
    elif token not in TREZOR_URLS_BY_TOKENS:
        return jsonify({"message": "unsupported token"})

    transaction = r.get("transaction")
    if not transaction:
        return jsonify({"message": "No transaction specified"})

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"}
    r = requests.get(TREZOR_URLS_BY_TOKENS[token] + f"tx-specific/{transaction}", headers=headers)
    if r.status_code == 200:
        return jsonify(r.json())

    return jsonify({})


@app.route("/transactions_info", methods=["POST"])
def transactions_info():
    r = request.get_json()
    transactions = r.get("transactions")
    if not transactions:
        return jsonify({"message": "No transactions specified"})

    token = r.get("token")
    if not token:
        return jsonify({"message": "token not specified"})
    elif token not in TREZOR_URLS_BY_TOKENS:
        return jsonify({"message": "unsupported token"})

    first_n = r.get("first_n", 100)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }

    resp = []
    for transaction in transactions[:first_n]:
        r = TRANSACTIONS_INFO_SESSION.get(TREZOR_URLS_BY_TOKENS[token] + f"tx/{transaction}", headers=headers)
        if r.status_code == 200:
            json_data = r.json()
            if token in ["BTC", "BCH", "BTG", "DOGE"]:
                json_data.update({"total_in": sum(float(v_item["value"]) for v_item in json_data["vin"])})
                json_data.update({"total_out": sum(float(v_item["value"]) for v_item in json_data["vout"])})
            resp.append(json_data)

    return jsonify(resp)


@app.route("/check_address")
def check_address():
    token = request.args.get("token")
    if not token:
        return jsonify({"message": "token not specified"})
    if token not in TREZOR_URLS_BY_TOKENS:
        return jsonify({"message": "unsupported token"})

    address = request.args.get("address")
    if not address:
        return jsonify({"message": "address not specified"})

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }

    r = CHECK_ADDRESS_SESSION.get(TREZOR_URLS_BY_TOKENS[token] + f"address/{address}", headers=headers)
    if token == "BTG":
        print(r.text)
    if r.status_code == 200:
        return jsonify(r.json())
    else:
        return jsonify({})


if __name__ == "__main__":
    app.run("0.0.0.0", port=API_PORT)
