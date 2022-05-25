from enum import Enum
import random
import string

import requests


class AuthResponses(Enum):
    OK = 0
    VERIFY_LOGIN = 1
    REQUIRE_MFA = 1
    INVALID_MFA_TOKEN = 1
    INVALID_ACCOUNT = -1
    RATE_LIMITED = -1


class WebAccount():

    def __init__(self):
        # This gets replaced if they load an account from file
        self.headers = WebAccount._generateDeviceProfile()

        self.accessToken = ""

    def authenticate(self, username: string = "", password: string = "", mfa: string = None):

        self.username = username

        # Check if a mfa token is provided,
        # if its not proform a simple login
        if mfa == None:

            # Request authentication
            resp = self._makeAPICall(
                'authentication',
                data=f'{{"strategy":"local","username":"{self.username}","password":"{password}","totpType":"sms"}}'
            )

            # Account login verification required
            if resp.status_code == 403:
                return AuthResponses.VERIFY_LOGIN

            # Invalid email or password
            if resp.status_code == 401:
                return AuthResponses.INVALID_ACCOUNT

            # Authentication token successfully requested
            if resp.status_code == 201:
                self.accessToken = resp.json()['accessToken']

                # Check to see if they need a MFA token
                if self._checkMFA():
                    return AuthResponses.REQUIRE_MFA

                return AuthResponses.OK

            if resp.status_code == 429:
                return AuthResponses.RATE_LIMITED

        # If an mfa token is provided, preform a mfa login
        if mfa != None:
            data = f'{{"strategy":"mfa","mfaToken":"{mfa}"}}'

            resp = self._makeAPICall('authentication', data)

            # Authentication token successfully requested
            if resp.status_code == 201:
                self.accessToken = resp.json()['accessToken']
                return AuthResponses.OK

            # MFA token was invalid
            if resp.status_code == 401:
                return AuthResponses.INVALID_MFA_TOKEN

    def basic_login(self):

        last_auth_responce = AuthResponses.INVALID_ACCOUNT
        password = ""

        while last_auth_responce != AuthResponses.OK:

            if last_auth_responce == AuthResponses.RATE_LIMITED or last_auth_responce == AuthResponses.INVALID_ACCOUNT:
                print("Username: ", end="")
                self.username = input()

                print("Password: ", end="")
                password = input()

            last_auth_responce = self.authenticate(self.username, password)

            match last_auth_responce:
                case AuthResponses.VERIFY_LOGIN:
                    print("Check your email to allow access then press enter...")
                    input()
                    last_auth_responce = self.authenticate(
                        self.username, password, mfa)
                case AuthResponses.REQUIRE_MFA:
                    print("Enter MFA code: ", end="")
                    mfa = input()

                    last_auth_responce = self.authenticate(
                        self.username, password, mfa)

                    if last_auth_responce == AuthResponses.INVALID_MFA_TOKEN:
                        print("Invalid MFA code")
                case _:
                    print(f"An error has occurred: {last_auth_responce}")

        print("Success!")

    def _checkMFA(self):
        resp = self._makeAPICall('wallets', '')

        response = resp.json()

        if response["name"] == "NotAuthenticated":
            return True
        return False

    def _makeAPICall(self, path, data):
        return requests.post(
            url=f'https://api.shakepay.com/{path}',
            headers=self.headers,
            data=data
        )

    def _generateDeviceProfile():

        def generateRandomText(length):
            temp = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][random.randint(0, 25)] for x in range(length)]
            return ''.join([temp[n].upper() if random.randint(0, 1) == 1 else temp[n] for n in range(length)])

        def generateRandomID(length, caplocks=False):
            temp = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'][random.randint(0, 35)] for x in range(length)]
            return ''.join([temp[n].upper() if random.randint(0, 1) == 1 or caplocks else temp[n] for n in range(length)])

        return {
            'Host': 'api.shakepay.com',
            'x-device-serial-number': '',
            'x-device-name': generateRandomText(11),
            'x-device-has-notch': 'false',
            'User-Agent': 'Shakepay App v1.7.24 (17024) on Apple iPhone 8 (iOS 14.6)',
            'x-device-locale': 'en-CA',
            'x-device-manufacturer': 'Apple',
            'x-device-is-tablet': 'false',
            'x-device-total-disk-capacity': '63978983424',
            'x-device-system-name': 'ShakePi | Created by',
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
            'x-device-unique-id': f'{generateRandomID(8, True)}-{generateRandomID(4, True)}-{generateRandomID(4, True)}-{generateRandomID(4, True)}-{generateRandomID(12, True)}',
            'x-notification-token': f'{generateRandomID(22, False)}:{generateRandomID(116, False)}_{generateRandomID(10, False)}-{generateRandomID(12, False)}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-device-brand': 'Apple',
            'Accept-Encoding': 'gzip, deflate, br',
            'x-device-system-version': 'Quzique',
        }
