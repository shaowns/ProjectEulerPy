# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:27:34 2015

@author: ShaownS
"""
very_large_number = 600851475143

def getLargestPrimeFactor(number):
    factor = 2
    while (factor < number):
        if (number % factor == 0):
            number /= factor
            factor = 2
        else:
            factor += 1
            
    return factor
    
def main():
    print getLargestPrimeFactor(very_large_number)
    return 0

if __name__ == '__main__':
    main()