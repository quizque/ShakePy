import requests
import json

"""Get information about the wait list"""
def getWaitlistInfo(account):
    resp = requests.get(
        url='https://api.shakepay.com/card/waitlist',
        headers=account,
        data='{}'
    )

    return json.loads(resp.text)

"""Enter the wait list"""
def enterWaitlist(account):
    resp = requests.post(
        url='https://api.shakepay.com/card/waitlist',
        headers=account,
        data='{}'
    )

    return json.loads(resp.text)