import json
import random
import requests
from os import error

"""Sign into shakepay account using a given username and password.

returns dictionary which will contain an error if status is -1.

VERIFY_LOGIN_EMAIL -> Check emails to approve login, then rerun the method with the returned account.
INVALID_ACCOUNT -> Account username/password combonation doesn't exist.
REQUIRE_MFA -> MFA Token is required, rerun with the returned account and MFA token.
API_RATE_LIMITED -> Cloudflair has banned your IP, you are being rate limited.
INVALID_MFA_TOKEN -> MFA token is invalid
"""
def authenticate(username, password, account=None, mfa=None):

    # Check if a mfa token is provided,
    # if its not proform a simple login
    if mfa == None:

        # If an account is passed, use it insted
        if account == None:
            # Generate a fake device to attach authentication to
            profile = __generateDeviceProfile()
        else:
            profile = account
        
        # Request authentication
        resp = requests.post(
            url='https://api.shakepay.com/authentication',
            headers=profile,
            data=f'{{"strategy":"local","username":"{username}","password":"{password}","totpType":"sms"}}'
        )

        # Account login verification required
        if resp.status_code == 403:
            return {"status": -1, "authentication": profile, "error": "VERIFY_LOGIN_EMAIL"}

        # Invalid email or password
        if resp.status_code == 401:
            return {"status": -1, "error": "INVALID_ACCOUNT"}

        # Authentication token successfully requested
        if resp.status_code == 201:
            profile['Authorization'] = json.loads(resp.text)['accessToken']

            # Check to see if they need a MFA token
            if __checkMFA(profile):
                return {"status": -1, "authentication": profile, "error": "REQUIRE_MFA"}

            return {"status": 1, "authentication": profile}
        
        if resp.status_code == 429:
            return {"status": -1, "error": "API_RATE_LIMITED"}

    # If a mfa token is provided,
    # proform a mfa login
    if mfa != None:
        data = f'{{"strategy":"mfa","mfaToken":"{mfa}"}}'

        resp = requests.post(
            url='https://api.shakepay.com/authentication',
            headers=account,
            data=data
        )


        # Authentication token successfully requested
        if resp.status_code == 201:
            account['Authorization'] = json.loads(resp.text)['accessToken']
            return {"status": 1, "authentication": account}

        # MFA token was invalid
        if resp.status_code == 401:
            return {"status": -1, "error": "INVALID_MFA_TOKEN"}
        



"""Saves authentication data with given name."""
def saveAccount(auth, filename):
    try:
        with open(f'{filename}.json', 'w') as file:
            json.dump(auth, file)
    except:
        error(f"Unable to write {filename}.json!")

"""Loads authentication data with given name."""
def loadAccount(filename):
    try:
        with open(f'{filename}.json', 'r') as file:
            return json.load(file)
    except:
        error(f"Unable to load {filename}.json!")


#######################################################################################################################################


"""Check for multifactor authentication (PRIVATE).

Return true if MFA code is needed, false otherwise."""
def __checkMFA(account):
    resp = requests.get(
        url='https://api.shakepay.com/wallets',
        headers=account,
        data=''
    )

    responce = json.loads(resp.text)

    if responce["name"] == "NotAuthenticated":
        return True
    return False

"""Generate a fake phone profile (PRIVATE)."""
def __generateDeviceProfile():
    return {
        'Host': 'api.shakepay.com',
        'x-device-serial-number': '',
        'x-device-name': __generateRandomText(11),
        'x-device-has-notch': 'false',
        'User-Agent': 'Shakepay App v1.7.24 (17024) on Apple iPhone 8 (iOS 14.6)',
        'x-device-locale': 'en-CA',
        'x-device-manufacturer': 'Apple',
        'x-device-is-tablet': 'false',
        'x-device-total-disk-capacity': '63978983424',
        'x-device-system-name': 'Created by',
        'x-device-carrier': ['Koodo', 'Telus', 'React', 'NextJS', 'Public', 'v8engine'][random.randint(0, 5)],
        'x-device-model': 'Python API Interface',
        'x-device-id': 'iPhone10,4',
        'x-device-total-memory': '2070495232',
        'x-device-country': 'CA',
        'x-device-mac-address': '02:00:00:00:00:00',
        'Connection': 'keep-alive',
        'x-device-tzoffset': '240',
        'Accept-Language': 'en-ca',
        'x-device-ip-address': f'192.168.1.{random.randint(5,200)}',
        'x-device-unique-id': f'{__generateRandomID(8, True)}-{__generateRandomID(4, True)}-{__generateRandomID(4, True)}-{__generateRandomID(4, True)}-{__generateRandomID(12, True)}',
        'x-notification-token': f'{__generateRandomID(22, False)}:{__generateRandomID(116, False)}_{__generateRandomID(10, False)}-{__generateRandomID(12, False)}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-device-brand': 'Apple',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-device-system-version': 'Quzique',
    }

"""Used to generate authentication data (PRIVATE)."""
def __generateRandomText(length):
        temp = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][random.randint(0,25)] for x in range(length)]
        return ''.join([temp[n].upper() if random.randint(0, 1) == 1 else temp[n] for n in range(length)])

"""Used to generate authentication data (PRIVATE)."""
def __generateRandomID(length, caplocks=False):
    temp = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'][random.randint(0,35)] for x in range(length)]
    return ''.join([temp[n].upper() if random.randint(0, 1) == 1 or caplocks else temp[n] for n in range(length)])
