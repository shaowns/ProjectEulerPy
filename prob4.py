def is_palindrome(n):
    number_string = str(n)
    reverse_string = reversed(number_string)
    return list(number_string) == list(reverse_string)


def main():
    largest = 0
    for i in xrange(999, 100, -1):
        # It suffices to check j till i, otherwise we do some multiplication more than once.
        for j in xrange(999, i+1, -1):
            number = i*j
            if number < largest:
                # There is no chance for j to catch up with the largest,
                # try with next i.
                break

            if is_palindrome(number) and number > largest:
                largest = number

    print largest
    return 0


if __name__ == '__main__':
    main()


