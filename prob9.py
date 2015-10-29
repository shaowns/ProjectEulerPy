from math import sqrt


def get_triplet_sum(n, m):
    return 2 * (n ** 2 + n * m)


def get_triplet_product(n, m):
    return (n ** 2 - m ** 2) * (2 * n * m) * (n ** 2 + m ** 2)


# Returns the product of the Pythagorean triplet a, b, c; where sum(a,b,c) = limit. -1 otherwise.
def get_largest_triplet_product(limit):
    # Start at n = 2, m = 1 and slowly grow out.
    j = 2
    while j < int(sqrt(limit)):
        i = 1
        while i < j:
            if get_triplet_sum(j, i) == limit:
                print j, i
                return get_triplet_product(j, i)
            i += 1
        j += 1

    # No such triplet exists.
    return -1


def main():
    print get_largest_triplet_product(1000)
    return 0


if __name__ == '__main__':
    main()