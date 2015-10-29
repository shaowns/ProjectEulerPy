from euler_utility import is_prime_eff, prime_sieve


def get_prime_sum(limit):
    # Start with the first prime.
    prime_sum = 2
    for x in xrange(3, limit + 1, 2):
        if is_prime_eff(x):
            prime_sum += x

    return prime_sum


def get_prime_sum_sieve(limit):
    sieve = prime_sieve(limit)
    prime_sum = 0
    for i in xrange(2, limit + 1):
        if not sieve[i]:
            prime_sum += i

    return prime_sum


def main():
    print get_prime_sum(2000000)
    print get_prime_sum_sieve(2000000)
    return 0


if __name__ == '__main__':
    main()
