from math import sqrt
from itertools import count, islice


# Basic prime checking function that is somewhat efficient.
def is_prime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n)-1)))
