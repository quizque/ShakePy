from email.quoprimime import unquote
import enum


@enum.unique
class Status(enum.Enum):
    VERIFY_LOGIN_EMAIL = 0
    INVALID_ACCOUNT = 1
    REQUIRE_MFA = 2
    API_RATE_LIMITED = 3
    INVALID_MFA_TOKEN = 4


def add_one(number):
    return number + 1
