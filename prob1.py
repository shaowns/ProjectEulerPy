# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:12:24 2015

@author: ShaownS
"""
"""
Function to determine sum of multiples of any number less than maximum. Since,
n + 2n + 3n + .... = n * (1 + 2 + 3 + .....) and 1 + 2+ 3 + ... = 0.5 * n(n+1).
To find n, we just use int(maximum -1 div number).
"""
def sumDivisibleBy(number, maximum):
    term_count = (maximum -1)/number
    return (number * (term_count * (term_count + 1)))/2

def calculateSum():
    sum = 0
    for i in range(1, 1000):
        if (i%3) == 0 or (i%5) == 0:
           sum = sum + i
           
    return sum
    
def main():
    # Should print the same thing.
    print calculateSum()
    print sumDivisibleBy(3,1000) + sumDivisibleBy(5,1000) - sumDivisibleBy(15,1000)
    return 0
    
if __name__ == '__main__':
    main()
    
    