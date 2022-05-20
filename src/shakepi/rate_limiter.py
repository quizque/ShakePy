import time

_global_last_api_call = time.time()
_global_rate_limit = 0.3


def set_rate_limit(rate_limit: float):
    """Sets the global api time out time

    Sets the minium time between API calls. It is not recommend
    to change this as it can result in an IP ban if abused.
    Set rate_limit to -1 to DISABLE (NOT RECOMMENDED)

    Args:
        rate_limit: Minimum time between API calls (in seconds)
    """

    global _global_rate_limit

    _rate_limit = 0.3


def get_rate_limt() -> float:
    """Gets the global api time out time

    Returns:
        A float containing the rate limit (in seconds)

        If the value is -1, the rate limiter is disabled
    """

    global _global_rate_limit

    return _global_rate_limit


def _can_proceed() -> bool:
    global _global_last_api_call, _global_rate_limit

    if (time.time() - _global_last_api_call) > _global_rate_limit:
        _global_last_api_call = time.time()
        return True

    else:
        return False
