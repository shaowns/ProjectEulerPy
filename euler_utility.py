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


# Basic implementation of sieve of Eratosthenes.
def prime_sieve(limit):
    cross_limit = int(sqrt(limit))
    sieve = [False for _ in xrange(0, limit + 1)]

    # For ease of implementation start with 0 index, 0 and 1 are not prime.
    sieve[0] = True
    sieve[1] = True

    # Mark out even numbers starting from 4.
    for n in xrange(4, limit + 1, 2):
        sieve[n] = True

    # Start with 3 and work with odd numbers up to the cross limit.
    for i in xrange(3, cross_limit + 1, 2):
        if not sieve[i]:
            # Sieve is not marked here.
            for j in xrange(i ** 2, limit + 1, 2 * i):
                sieve[j] = True

    return sieve
