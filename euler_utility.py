from math import sqrt
from itertools import count, islice


# Basic prime checking function that is somewhat efficient.
def is_prime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n)-1)))


# More efficient prime checker.
def is_prime_eff(n):
    if n <= 1:
        # 1 is not prime.
        return False
    elif n < 4:
        # 2 and 3 are prime.
        return True
    elif n % 2 == 0:
        # Evens are not prime.
        return False
    elif n < 9:
        # We ruled out 4,6,8 above.
        return True
    elif n % 3 == 0:
        return False
    else:
        from math import sqrt, floor
        limit = int(floor(sqrt(n)))

        # Start checking at 5.
        factor = 5
        while factor <= limit:
            if n % factor == 0:
                return False
            elif n % (factor + 2) == 0:
                return False
            else:
                # Every prime greater than 3 can be expressed as 6*k +/- 1.
                factor += 6

        # Reached here, must be prime.
        return True
