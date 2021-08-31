import shakepay_api

# quick auth an account
account = shakepay_api.quick_auth("account1")

print("Attempting to trigger shaking sats...")

# Trigger the shaking sats request
rslt = shakepay_api.triggerShakingSats(account)

# The prize has been redeemed today already
if rslt['code'] == 409:
    print(f"Prize already redeemed! Current streak: {rslt['data']['streak']}")

# We have successess fully claimed the prize
else:
    print(f"Prize redeemed! Current streak: {rslt['data']['streak']}")