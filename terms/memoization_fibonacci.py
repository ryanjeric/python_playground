# MEMOIZATION using lru_cache
from functools import lru_cache
#fibonacci_cache = {}
@lru_cache(maxsize=1000)
def fibonacci(n):
    # if found on cache return
    #if n in fibonacci_cache:
    #    return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    # Cache the value and return it
    #fibonacci_cache[n] = value
    return value

for n in range(1,1000):
    print(n, ": ", fibonacci(n))


