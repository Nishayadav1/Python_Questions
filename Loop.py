# N times "Hello World":
# You are given an integer n. Print "Hello World" n times.
# Sample Input: 
# 5
# Sample Output: 
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# -------------------------------ans-----------------------

# n=int(input())
# i=0 
# while n>i:
#     print("Hello World")
#     i+=1

# ----------------------------------------------------

# N times * in the same line:
# You are given an integer n. Print * n times in the same line with space in between.
# Sample Input: 
# 5
# Sample Output: 
# * * * * *

# ---------------ans-----------------------

# n=int(input())
# i=0 
# while n>i:
#     print("*",end=" ")
#     i+=1

# --------------------------------------





# First n Natural Numbers:
# You are given an integer n. Print the first n natural numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 2 3 4 5 6 7

# -----------------ans-----------------------------
# n=int(input())
# i=1 
# while n>=i:
#     print(i,end=" ")
#     i+=1
    
    
# -------------------------------------------------------    


# All Even Numbers till n:
# You are given an integer n. Print all the even numbers less than equal to n.
# Sample Input: 
# 14
# Sample Output: 
# 2 4 6 8 10 12 14


# ------------------------ans-----------------------------

# n=int(input())
# i=1 
# while n>=i:
#     if i%2==0:
#         print(i,end=" ")
#     i+=1    

# -----------------------------------------------------

# All Square Numbers till n:
# You are given an integer n. Print all the square numbers less than equal to n.
# Sample Input: 
# 50
# Sample Output: 
# 1 4 9 16 25 36 49

# -----------------------------ans------------------------------------
# n=int(input())
# i=1 
# while n>=i*i:
#     print(i*i,end=" ")
#     i+=1

# ------------------------------------------------------------

# First n Even Numbers:
# You are given an integer n. Print the first n even numbers.
# Sample Input: 
# 7
# Sample Output: 
# 2 4 6 8 10 12 14

# -----------------------------ans------------------------------------
# n=int(input())
# c=0
# i=1
# while True:
#     if i%2==0:
#         print(i,end=" ")
#         c+=1
#         if c==n:
#             break
        
#     i+=1    
        

# ----------------------------------------------------------------

# First n Odd Numbers:
# You are given an integer n. Print the first n odd numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 3 5 7 9 11 13

# --------------------ans------------------------------
# n=int(input())
# c=0
# i=1
# while True:
#     if i%2!=0:
#         print(i,end=" ")
#         c+=1
#         if c==n:
#             break
        
#     i+=1  
# -------------------------------------------------------

# First n Square Numbers:
# You are given an integer n. Print the first n square numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 4 9 16 25 36 49


# --------------------ans------------------------------
# n=int(input())
# i=1
# while n>=i:
#     print(i*i,end=" ")   
#     i+=1

# -----------------------------------------------------


# Multiplication Table of n:
# You are given an integer n. Print the multiplication table of n till count 10.
# Sample Input: 
# 7
# Sample Output: 
# 7 14 21 28 35 42 49 56 63 70
# Explanation: Print 7*1, 7*2, …, 7*10.

# -----------------------ans------------------------------------
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
# n=int(input())
# i=1
# while 10>=i:
#     # print(n,"*",i,"=",n*i)
#     print(n*i,end= " ")
#     i+=1

# -----------------------------------------------------------

# Factors of a Number:
# Write a program that takes a number n as input and prints all the factors of the number.
# Sample Input: 
# 24
# Sample Output: 
# 1 2 3 4 6 8 12 24
# Explanation: The factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24.

# -----------------------ans----------------------------
# n=int(input())
# i=1 
# while n>=i:
#     if n%i==0:
#         print(i,end=" ")
#     i+=1    

# --------------------------------------------------- 


# Series: 3, 5, 7, 9, 11, …:
# You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…
# Sample Input: 
# 7
# Sample Output: 
# 3 5 7 9 11 13 15
# Explanation: The series starts with 3 and every time adds 2 to get the next term.

# ------------------------------ans-----------------------------------------

# n=int(input())
# i=3 
# c=0
# while True:
#     print(i,end=" ")
#     c+=1
#     if c==n:
#         break
#     i+=2

# -------------------------------------------------------------------
# Series: 2, 5, 8, 11, 14, …:
# You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…
# Sample Input: 
# 7
# Sample Output: 
# 2 5 8 11 14 17 20
# Explanation: The series starts with 2 and every time adds 3 to get the next term.

# ----------------------------ans-----------------------------------
# n=int(input())
# i=2 
# c=0
# while True:
#     print(i,end=" ")
#     c+=1
#     if c==n:
#         break
#     i+=3

# --------------------------------------------------------------

# Series: 3, 6, 12, 24, 48, …:
# You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
# Sample Input: 
# 7
# Sample Output: 
# 3 6 12 24 48 96 192
# Explanation: The series starts with 3 and every time multiplies 2 to get the next term.

# ------------------------ans-----------------------------------------------
# n=int(input())
# i=3 
# c=0
# while True:
#     print(i,end=" ")
#     c+=1
#     if c==n:
#         break
#     i+=i

# ------------------------------------------------------------------------

# Sum of First n Natural Numbers:
# You are given an integer n. Print the sum of the first n Natural Numbers.
# Note: Use a loop instead of a mathematical formula.
# Sample Input: 
# 7
# Sample Output: 
# 28
# Explanation: Sum of 1+2+3+4+5+6+7 = 28

# ---------------------------ans------------------------------------------
# n=int(input())
# s=0 
# i=1 
# while 7>=i:
#     s+=i
#     i+=1
# print(s)    


# ---------------------------------------------------------

# Sum of Series: 3, 5, 7, 9, 11, …:
# You are given an integer n. Print the sum of the first n terms of the series 3, 5, 7, 9, 11….
# Note: Use a loop instead of a mathematical formula.
# Sample Input: 
# 7
# Sample Output: 
# 63
# Explanation: Sum of 3+5+7+9+11+13+15 = 63

# --------------------------ans---------------------------------
# n=int(input())
# i=3 
# c=0
# s=0 
# while True:
#     s+=i
#     c+=1
#     if c==n:
#         break
#     i+=2
    
# print(s)    
    

# -----------------------------------------------------------------

# Factorial of a Number:
# Write a program to calculate the factorial of a given number n. 
# The factorial of a number n is the product of all positive integers less than or equal to n.
# Sample Input: 
# 6
# Sample Output: 
# 720
# Explanation: 720 = 6*5*4*3*2*1

# -------------------ans-----------------------------

# n=int(input())
# i=1 
# m=1
# while n>=i:
#     m*=i 
#     i+=1
# print(m)    
    


# ---------------------------------------------------------------

# Counting Digits in a Number:
# Write a program that takes a number n as input and prints the number of digits the number has.
# Sample Input: 
# 1132
# Sample Output: 
# 4

# ---------------------ans--------------------------------
# n=int(input())
# i=0
# while n>0:
#     a=n%10
#     i+=1
#     n//=10
# print(i)    


# ----------------------------------------------------------

# Sum of Digits of a Number:
# Write a program that calculates the sum of all the digits in a given number n.
# Sample Input: 
# 1132
# Sample Output: 
# 7
# Explanation: 7 = 1+1+3+2  

# ---------------------------ans--------------------------------------
# n=int(input())
# i=0
# s=0
# while n>0:
#     a=n%10
#     s+=a
#     i+=1
#     n//=10
# print(s)  
# -----------------------------------------------------------------