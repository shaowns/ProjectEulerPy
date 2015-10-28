from itertools import count

import euler_utility as eu


def get_nth_prime(n):
    # Cutting corners, problem gives 6 primes, starting at there.
    prime_count = 6
    current_prime = 13

    for x in count(current_prime + 2):
        if eu.is_prime_eff(x):
            current_prime = x
            prime_count += 1

            if prime_count == n:
                break

    return current_prime


def main():
    print get_nth_prime(10001)
    return 0


if __name__ == '__main__':
    main()
