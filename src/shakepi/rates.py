import requests
import json

"""Get the most recent shakepay rates"""
def getRates(account):
    resp = requests.get(
        url='https://api.shakepay.com/rates',
        headers=account,
        data='{}'
    )

    return json.loads(resp.text)

"""Get the current conversion quote with or without fees"""
def getQuote(account, include_fees=True):
    resp = requests.get(
        url=f'https://api.shakepay.com/quote?includeFees={include_fees}',
        headers=account,
        data='{}'
    )

    return json.loads(resp.text)

"""Get historical rates

pair -> Must be CAD_ETH, CAD_BTC or the other way around
from_date/to_date -> Must be formatted as 2021-08-30T07:42:46.199Z (year-month-dayTtimeZ)
window -> Time per day? Recommended to set as '15m' (UNKNOWN).
"""
def getHistoricalRates(account, pair, from_date, to_date, window):
    resp = requests.post(
        url='https://api.shakepay.com/rates/history',
        headers=account,
        data=f'{{"pair": "{pair}","fromDate": "{from_date}","toDate": "{to_date}","window": "{window}"}}'
    )

    return json.loads(resp.text)