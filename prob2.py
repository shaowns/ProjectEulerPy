# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:18:22 2015

@author: ShaownS
"""
input_number = 4000000

def fibSum(maximum):
    sum = 0
    prev = 1
    current = 2
    while (current <= maximum):
        if (current % 2) == 0:
            sum = sum + current
        
        # Get the next Fibonacci number in the series and store the current into
        # the previous one.
        temp = current + prev
        prev = current
        current = temp
        
    return sum
    
def main():
    print fibSum(input_number)
    return 0

if __name__ == '__main__':
    main()