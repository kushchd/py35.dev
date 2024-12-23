#
import time
from functools import wraps

def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting for {seconds} seconds before calling {func.__name__}...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(5)
def it_may_be(name=''):
    return (name + " ask: It's nearly Luncheon Time? \n")

# Приклад використання
for t in range(12):
    print(it_may_be(name='Winnie-the-Pooh'))
print("The program has completed.")
