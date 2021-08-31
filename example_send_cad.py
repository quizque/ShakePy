import shakepay_api

###
### WARNING
### WARNING
### WARNING
### WARNING
### WARNING
###
### This script sends REAL currency, don't use if you don't understand what its doing!
###

print("Attempting to use quick_auth() to get authentication...")

# quick_auth is an already programmed function that will request an accounts auth information
# if it doesn't already exist at the given file
account = shakepay_api.quick_auth("account1")

# Try to send 1$ to @hammy5030
transaction = shakepay_api.sendCAD(account, "hammy5030", 1, "Hello World!")

# Print the transaction information
print(f"Transaction information: {transaction}")