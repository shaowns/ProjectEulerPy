from euler_utility import is_prime


# Gives the list of primes below n.
def get_prime_list(n):
    if n < 2:
        return []

    # Add 2 by default, for efficient looping.
    prime_list = [2]
    for x in xrange(3, n+1, 2):
        if is_prime(x):
            prime_list.append(x)

    return prime_list


# Returns the maximum power of the given prime that divides the given number.
def prime_power(number, prime):
    power = 0
    while number % prime == 0:
        number /= prime
        power += 1

    return power


def get_evenly_divisible_number(n):
    # List of prime numbers less than n.
    primes = get_prime_list(n)

    prime_powers = {}
    for x in xrange(1, 21):
        if x in primes:
            prime_powers[x] = 1
        else:
            for prime in primes:
                if prime > x:
                    break
                prime_powers[prime] = max(prime_powers[prime], prime_power(x, prime))

    result = 1
    for prime in primes:
        result *= prime ** prime_powers[prime]

    return result


def main():
    print get_evenly_divisible_number(20)
    return 0


if __name__ == '__main__':
    main()
