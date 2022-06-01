from shakepay_api.wallet import getBTCWalletID, getCADWalletID, getETHWalletID
import requests
import json

"""Get past transaction history"""
def getTransactionHistory(account, currency, rowsPerPage=200, page=1):
    resp = requests.post(
        url='https://api.shakepay.com/transactions/history',
        headers=account,
        data=f'{{"pagination":{{"descending":true,"rowsPerPage":{rowsPerPage},"page":{page}}},"filterParams":{{"currencies":["{currency}"]}}}}'
    )

    return json.loads(resp.text)

"""Send BTC to an address"""
def sendBTC(account, address, amount):
    resp = requests.post(
        url=f'https://api.shakepay.com/transactions',
        headers=account,
        data=f'{{"amount":"{amount}","note":"","fromWallet":"{getBTCWalletID(account)}","to":"{address}","toType":"crypto"}}'
    )

    return json.loads(resp.text)

"""Send ETH to an address"""
def sendETH(account, address, amount):
    resp = requests.post(
        url=f'https://api.shakepay.com/transactions',
        headers=account,
        data=f'{{"amount":"{amount}","note":"","fromWallet":"{getETHWalletID(account)}","to":"{address}","toType":"crypto"}}'
    )

    return json.loads(resp.text)

"""Send CAD to another user"""
def sendCAD(account, user, amount, note):
    resp = requests.post(
        url=f'https://api.shakepay.com/transactions',
        headers=account,
        data=f'{{"amount":"{amount}","note":"{note}","fromWallet":"{getCADWalletID(account)}","to":"{user}","toType":"user"}}'
    )

    return json.loads(resp.text)

"""Get recent contacts"""
def getRecentContacts(account):
    resp = requests.get(
        url='https://api.shakepay.com/recent-contacts',
        headers=account,
        data=''
    )

    return json.loads(resp.text)

"""Convert from one currency to another"""
def convert(account, from_wallerid, to_walletid, from_amount):
    resp = requests.post(
        url='https://api.shakepay.com/conversions',
        headers=account,
        data=f'{{"fromWalletId":"{from_wallerid}","toWalletId":"{to_walletid}","fromAmount":{from_amount}}}'
    )

    return json.loads(resp.text)