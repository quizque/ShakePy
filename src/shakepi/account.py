import random
import time


class Account:
    """Shakepay account class.

    Used to store information about a Shakepay account
    to be used with API calls in order to retrieve information

    Attributes:
        timeout: Internal API timeout rate (recommend to leave at default)

    """

    def __init__(self, timeout: float = 1):
        self.http_headers = Account._generate_http_headers()
        self.timeout = timeout
        self._timeout_counter = time.time()

    def _generate_http_headers():
        return {
            "Host": "api.shakepay.com",
            "x-device-serial-number": "",
            "x-device-name": Account._generateRandomText(11),
            "x-device-has-notch": "false",
            "User-Agent": "Shakepay App v1.7.24 (17024) on Apple iPhone 8 (iOS 14.6)",
            "x-device-locale": "en-CA",
            "x-device-manufacturer": "Apple",
            "x-device-is-tablet": "false",
            "x-device-total-disk-capacity": "63978983424",
            "x-device-system-name": "ShakePi -",
            "x-device-carrier": [
                "Koodo",
                "Telus",
                "React",
                "NextJS",
                "Public",
                "v8engine",
            ][random.randint(0, 5)],
            "x-device-model": "Python API Interface",
            "x-device-id": "iPhone10,4",
            "x-device-total-memory": "2070495232",
            "x-device-country": "CA",
            "x-device-mac-address": "02:00:00:00:00:00",
            "Connection": "keep-alive",
            "x-device-tzoffset": "240",
            "Accept-Language": "en-ca",
            "x-device-ip-address": f"192.168.1.{random.randint(5,200)}",
            "x-device-unique-id": f"{Account._generateRandomID(8, True)}-{Account._generateRandomID(4, True)}-{__generateRandomID(4, True)}-{__generateRandomID(4, True)}-{__generateRandomID(12, True)}",
            "x-notification-token": f"{Account._generateRandomID(22, False)}:{Account._generateRandomID(116, False)}_{__generateRandomID(10, False)}-{__generateRandomID(12, False)}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-device-brand": "Apple",
            "Accept-Encoding": "gzip, deflate, br",
            "x-device-system-version": f"Login Request",
        }

    def _generateRandomText(length):
        temp = [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",][random.randint(0, 25)]  for x in range(length)]  # fmt: skip
        return "".join(
            [
                temp[n].upper() if random.randint(0, 1) == 1 else temp[n]
                for n in range(length)
            ]
        )

    def _generateRandomID(length, caplocks=False):
        temp = [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"][random.randint(0, 35)]for x in range(length)]  # fmt: skip
        return "".join(
            [
                temp[n].upper() if random.randint(0, 1) == 1 or caplocks else temp[n]
                for n in range(length)
            ]
        )
