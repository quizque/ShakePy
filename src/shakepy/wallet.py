import requests
import json

"""Get the wallets"""
def getWallets(account):
    resp = requests.get(
        url='https://api.shakepay.com/wallets',
        headers=account,
        data=''
    )

    return json.loads(resp.text)

"""Get ETH wallet id"""
def getETHWalletID(account):
    resp = requests.get(
        url='https://api.shakepay.com/wallets',
        headers=account,
        data=''
    )

    return json.loads(resp.text)["data"][2]["id"]

"""Get BTC wallet id"""
def getBTCWalletID(account):
    resp = requests.get(
        url='https://api.shakepay.com/wallets',
        headers=account,
        data=''
    )

    return json.loads(resp.text)["data"][1]["id"]

"""Get CAD wallet id"""
def getCADWalletID(account):
    resp = requests.get(
        url='https://api.shakepay.com/wallets',
        headers=account,
        data=''
    )

    return json.loads(resp.text)["data"][0]["id"]

"""Get BTC address"""
def getBTCAddress(account):
    resp = requests.get(
        url=f'https://api.shakepay.com/wyre-wallets?walletId={getBTCWalletID(account)}',
        headers=account,
        data=''
    )

    return json.loads(resp.text)["data"][0]["address"]

"""Get ETH address"""
def getETHAddress(account):
    resp = requests.get(
        url=f'https://api.shakepay.com/wyre-wallets?walletId={getETHWalletID(account)}',
        headers=account,
        data=''
    )

    return json.loads(resp.text)["data"][0]["address"]