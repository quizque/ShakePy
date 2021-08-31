import shakepay_api


print("Attempting to use quick_auth() to get authentication...")

# quick_auth is an already programmed function that will request an accounts auth information
# if it doesn't already exist at the given file
account = shakepay_api.quick_auth("account1")

# Get information on the wallet from the account we just authenticated
wallets = shakepay_api.getWallets(account)

print(shakepay_api.getETHAddress(account))

print(f"Current CAD: {wallets['data'][0]['balance']}")
print(f"Current BTC: {wallets['data'][1]['balance']}")
print(f"Current ETH: {wallets['data'][2]['balance']}")