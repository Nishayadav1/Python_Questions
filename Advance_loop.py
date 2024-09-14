'''Fibonacci Series:
Write a program that takes a number n as input and prints the first n terms of the Fibonacci Series.
The Fibonacci Series is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
Sample Input: 
10
Sample Output: 
0 1 1 2 3 5 8 13 21 34 '''

# --------------------ans-------------------------------------

# n=int(input())
# a=0
# b=1
# i=1
# if n==1:
#     print(a)
# elif n==2:
#     print(a,b)
# else: 
#     print(a,b,end=" ")
#     while n-2>=i:
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#         i+=1

# -----------------------------------------------------------

'''
Reverse a Number:
Write a program that takes a number n as input and prints the reverse of the given number.
Sample Input: 
1132
Sample Output: 
2311
Explanation: The reverse of 1132 is 2311.
'''

# ------------------------------ans---------------------------
# n=int(input())
# s=0
# while n>0:
#     a=n%10
#     s=s*10+a
#     n//=10 
# print(s)  
    
# -------------------------------------------------------------

# GCD (Greatest Common Divisor) or HCF (Highest Common Factor):

'''
You are given two positive integers a and b. Print the GCD or HCF of these two numbers.
Sample Input: 
20 16
Sample Output: 
4
'''

# -----------------------ans---------------------------------------------
# a = int(input())
# b = int(input())
# m = 0
# if a > b:
#     limit = b
# else:
#     limit = a
# i = 1
# while i <= limit:
#     if a % i == 0 and b % i == 0:
#         m = i  
#     i += 1
# print(m)
 

# ----------------------or------------------
# a=int(input())
# b=int(input())
# while b>0:
#     a,b=b,a%b
# print(a)    
                   

# ---------------------------------------------------------------------

'''
LCM (Least Common Multiple):
You are given two positive integers a and b. Print the LCM of these two numbers.
Sample Input: 
20 16
Sample Output: 
80
'''
# ---------------------------ans-------------------------------------------------

# a = int(input())
# b = int(input())
# if a > b:
#     lcm = a
# else:
#     lcm = b
# while lcm % a != 0 or lcm % b != 0:
#     lcm += 1

# print("LCM is:", lcm)

            


# --------------------------------------------------------------------------
'''
Binary to Decimal:
Write a program that takes a Binary Number B as input and prints the Decimal equivalent of the given input.
Sample Input: 
1000
Sample Output: 
8
'''

# ---------------ans------------------------------------------
# b=int(input())
# d=0
# m=1
# while b>0:
#     a=b%10
#     d+=a*m
#     m*=2
#     b//=10
# print(d)    
# ---------------------------------------------------------

'''
Decimal to Binary:
Write a program that takes a Decimal Number D as input and prints the Binary equivalent of the given input.
Sample Input: 
8
Sample Output: 
1000
'''
# ---------------ans--------------------------------------------

# num=int(input())
# b=""
# if num==0:
#     print("0")
# while num>0:
#     a=num%2
#     b=str(a)+b
#     num//=2
# print(b)         

#--------or--------

# num=int(input())
# b=bin(num)[2:]
# print(b)

# -------------------------------------------------------------

'''
Is Prime?:
You are given an integer n. Print yes, if it is a prime number. Print no, if it is not a prime number.
Sample Input 1: 
49
Sample Output 1: 
No
Sample Input 2: 
37
Sample Output 2: 
Yes
'''

# ----------------------ans-------------------------------------
# n=int(input())
# i=1
# c=0
# while n>=i:
#     if n%i==0:
#         c+=1
#     i+=1    
# if c>2:
#     print("NO")
# else:
#     print("Yes")            
    
# ---------------------------------------------------------------

'''
Is Perfect Number?:
You are given an integer n. Print yes, if it is a Perfect Number. Print no, if it is not a Perfect Number.
A Perfect Number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
Sample Input 1: 
28
Sample Output 1: 
Yes
Explanation 1: The factors of 28 are 1, 2, 4, 7, 14, 28. We don't consider the number itself. 28 = 1+2+4+7+14.
Sample Input 2: 
24
Sample Output 2: 
No
Explanation 2: The factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24. We don't consider the number itself. But 24 != 1+2+3+4+6+8+12.
'''

# ----------------------ans-------------------------
# n=int(input())
# i=1 
# s=0
# while n>i:
#     if n%i==0:
#         s+=i
#     i+=1    
# if s==n:
#     print("yes")
# else:
#     print("No")            

# -----------------------------------------------------

'''
Is Armstrong Number?:
You are given an integer n. Print yes, if it is an Armstrong Number. Print no, if it is not an Armstrong Number.
An Armstrong Number is a positive number that equals the sum of its digits, each raised to the power of the number of digits.
Sample Input 1: 
1634
Sample Output 1: 
Yes
Explanation 1: 1634 has 4 digits, so we raise each digit to the power of 4. 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634 
Sample Input 2: 
153
Sample Output 2: 
Yes
Explanation 2: 153 has 3 digits, so we raise each digit to the power of 3. 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
'''

# n=int(input())
# m=n
# a=str(n)
# l=len(a)
# s=0 
# while n>0:
#     r=n%10
#     s+=r**l 
#     n//=10
# if s==m:
#     print('YES')
# else:
#     print("no")        
    
    
'''
Star Pattern 1:
Print the following pattern based on the given input.
Sample Input: 
6
Sample Output: 
*
**
***
****
*****
******
Explanation: Since the input is 6, it prints a total of 6 lines. In each line, the star count increases.
'''

# n=int(input())
# i=1 
# while n>=i:
#     print(i*"*")
#     i+=1

'''
Star Pattern 2:
Print the following pattern based on the given input.
Sample Input: 
6
Sample Output: 
     *
    **
   ***
  ****
 *****
******
Explanation: Since the input is 6, it prints a total of 6 lines. In each line, the star count increases and the leading space decreases.
'''

# n=int(input())
# i=1
# while n>=i:
#     print(" "*(n-i),i*"*")
#     i+=1



'''
Star Pattern 3:
Print the following pattern based on the given input.
Sample Input: 
6
Sample Output: 
*
 *
  *
   *
    *
     *
Explanation: Since the input is 6, it prints a total of 6 lines. In each line, it prints only one star, but the leading space increases.
'''

# n=int(input())
# i=0
# while n>i:
#     print(" "*i+"*")
#     i+=1


'''
Star Pattern 4:
Print the following pattern based on the given input.
Sample Input: 
5
Sample Output: 
    *
   ***
  *****
 *******
*********
Explanation: Since the input is 5, it prints a total of 5 lines of stars. Each line has stars as well as leading spaces. In each line, the star count increases by 2, but the leading space decreases by 1
'''
# n=int(input())
# i=0
# while n>i:
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
#     i+=1


'''
First n prime numbers:
You are given an integer n. Print the first n prime numbers.
Sample Input: 
7
Sample Output: 
2 3 5 7 11 13 17
'''
n = int(input())
i = 2  
m = 0  

while m < n:
    j = 1
    c = 0
    while j <= i:
        if i % j == 0:
            c += 1
        j += 1
    if c == 2:  
        m += 1
        print(i, end=" ")
    i += 1

        
    
                
    










