from os import error, path
import shakepay_api

"""Preprogrammed authorization sequence

Do not use this if you need more complex access to the API
"""
def quick_auth(filename):
    account = None
    mfa_token = None
    
    if path.isfile(f'{filename}.json'):
        print("Account file exists...")
        return shakepay_api.loadAccount(filename)

    while True:

        if account == None:
            email = input("Enter username: ")
            password = input("Enter password: ")

            result = shakepay_api.authenticate(email, password)
        
        elif mfa_token == None:
            result = shakepay_api.authenticate(email, password, account)

        else:
            result = shakepay_api.authenticate(email, password, account, mfa_token)

        if result['status'] == -1:
            if result['error'] == 'INVALID_ACCOUNT':
                error("Invalid account")
        
            if result['error'] == 'VERIFY_LOGIN_EMAIL':
                print("An email has been sent to verify the login, make sure to check spam.")
                input("Press enter to retry authentication after verifying login...")
                account = result['authentication']
                continue

            if result['error'] == 'REQUIRE_MFA':
                print("A MFA token is required, check your MFA app or SMS...")
                mfa_token = input("Input your MFA token: ")
                account = result['authentication']

            if result['error'] == 'INVALID_MFA_TOKEN':
                print("Invalid MFA token entered...")
                mfa_token = input("Input your MFA token: ")
            

            if result['error'] == 'API_RATE_LIMITED':
                print("You are being rate limited, try again later")
                exit()
        
        if result['status'] == 1:
            print(f"Successfully logged in, saving authentication profile as {filename}.json")
            shakepay_api.saveAccount(account, filename)
            return account