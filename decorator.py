"""
A decorator is a function that takes another function and returns a modified
version of it. They're commonly used to add cross-cutting behavior such as
logging, caching, retries, authentication, rate limiting, and timing without
changing the original function's code.
"""

import random
import time
from functools import wraps


def retry(max_attempts=3, delay=1):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attemp {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed: {e}")
                    last_exception = e

                    if attempt < max_attempts:
                        time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator


@retry(max_attempts=5, delay=0.5)
def fetch_user_profile(user_id):
    """
    Simulate an unreliable service.
    """
    if random.random() < 0.7:
        raise ConnectionError("Temporary network issue")

    return {"id": user_id, "name": "Alice"}


def main():
    try:
        # NOTE: similar to:
        # profile = retry(max_attempts=5, delay=0.5)(fetch_user_profile)(123)
        profile = fetch_user_profile(123)
        print("\nSuccess")
        print(profile)
    except Exception as e:
        print("\nOperation permanently failed")
        print(e)


if __name__ == "__main__":
    main()
