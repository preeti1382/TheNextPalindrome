'''
Date:25-11-2020
Author:Preeti Harjani
Purpose:Learning Python
'''
"""
Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222
"""

def reverse(n):
    rev = 0
    while n > 0:
            rem = n % 10  # Finding the remainder
            rev = (rev*10) + rem
            n = n//10  # Finding the quotient
    return rev

t = int(input("\nPlease enter number of testcases to be checked:"))
while t != 0:
    num = int(input("\nEnter number:"))
    temp = num
    let = False
    while let != True:
        r = reverse(num)
        if r == num:
            print(f"\nNext palindrome for {temp} is {r}")
            let = True
        else:
            num += 1
    t -= 1