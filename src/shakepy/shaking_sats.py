import requests
import json

"""Activate shacking sats"""
def triggerShakingSats(account):
    resp = requests.post(
        url='https://api.shakepay.com/shaking-sats',
        headers=account,
        data='{}'
    )

    return json.loads(resp.text)