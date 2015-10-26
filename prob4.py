def is_palindrome(n):
    number_string = str(n)
    reverse_string = reversed(number_string)
    return list(number_string) == list(reverse_string)


def main():
    palindromes = []
    for i in xrange(999, 100, -1):
        for j in xrange(999, 100, -1):
            number = i*j
            if is_palindrome(number):
                palindromes.append(number)

    palindromes.sort(key=int, reverse=True)
    print palindromes[0]
    return 0


if __name__ == '__main__':
    main()


