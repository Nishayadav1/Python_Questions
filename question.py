# Odd or Even:
# Write a program that takes a positive integer n as input and prints whether it is odd or even.
# Sample Input 1: 
# 49
# Sample Output 1: 
# Odd
# Sample Input 2: 
# 36
# Sample Output 2: 
# Even
# ---------------------------ans-----------------------------------
# num=int(input())
# if num%2==0:
#     print("even")
# else:
#     print("odd")    
    
 # --------------------------------------------------------------   
    
# Grading System:
# Write a program that takes a student's score (out of 100) and outputs their grade based on the following conditions:
# 90-100: Grade A
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D
# Below 60: Grade F
# Sample Input 1: 
# 78
# Sample Output 1: 
# C
# Sample Input 2: 
# 90
# Sample Output 2: 
# A
# Sample Input 3: 
# 48
# Sample Output 3: 
# F
# -------------------------ans--------------------------------
# grade = int(input())
# if 90 <= grade <= 100:
#     print("A")
# elif 80 <= grade <= 89:
#     print("B")    
# elif 70 <= grade <= 79:
#     print("C") 
# elif 60 <= grade <= 69:
#     print("D")
# elif grade < 60:
#     print("F")
# --------------------------------------------------------------
            
# Age Group Categorizer
# Write a program that categorizes a person's age into different life stages based on the following conditions:
# 0-2 years: Infant
# 3-12 years: Child
# 13-19 years: Teenager
# 20-65 years: Adult
# Above 65 years: Senior
# The program takes an age as input and prints the age group category the person belongs to. 
# Sample Input 1:
# 15
# Sample Output 1:
# Teenager
# Sample Input 2: 
# 2
# Sample Output 2: 
# Infant
# Sample Input 3: 
# 72
# Sample Output 3: 
# Senior

# ---------------------------ans-----------------------------------
age=int(input())







# --------------------------------------------------------------


# Temperature Adviser
# Write a program that suggests an activity based on the current temperature (in Celsius), following these guidelines:
# Above 30°C: "It's hot. Let's go swimming!"
# 20°C to 30°C: "Perfect for a picnic."
# 10°C to 19°C: "Maybe wear a jacket?"
# Below 10°C: "Too cold! Best to stay indoors."
# The program takes the current temperature as input and prints the suggested activity.
# Sample Input 1: 
# 15
# Sample Output 1: 
# Maybe wear a jacket?
# Sample Input 2: 
# 8
# Sample Output 2: 
# Too cold! Best to stay indoors.
# Sample Input 3: 
# 38
# Sample Output 3: 
# It's hot. Let's go swimming!





# Maximum of Three Numbers:
# Write a program that takes three numbers as input and prints the largest number.
# Sample Input 1: 
# 15 23 16
# Sample Output 1: 
# 23
# Sample Input 2: 
# 8 5 9
# Sample Output 2: 
# 9




# Sort Three Numbers
# Write a program that takes three numbers as input and prints the numbers in ascending order.
# This program doesn't use an array.
# Sample Input 1: 
# 15 23 16
# Sample Output 1: 
# 15 16 23
# Sample Input 2: 
# 8 5 9
# Sample Output 2: 
# 5 8 9





# Loops
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





# N times * in the same line:
# You are given an integer n. Print * n times in the same line with space in between.
# Sample Input: 
# 5
# Sample Output: 
# * * * * *





# First n Natural Numbers:
# You are given an integer n. Print the first n natural numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 2 3 4 5 6 7







# All Even Numbers till n:
# You are given an integer n. Print all the even numbers less than equal to n.
# Sample Input: 
# 14
# Sample Output: 
# 2 4 6 8 10 12 14





# All Square Numbers till n:
# You are given an integer n. Print all the square numbers less than equal to n.
# Sample Input: 
# 50
# Sample Output: 
# 1 4 9 16 25 36 49





# First n Even Numbers:
# You are given an integer n. Print the first n even numbers.
# Sample Input: 
# 7
# Sample Output: 
# 2 4 6 8 10 12 14






# First n Odd Numbers:
# You are given an integer n. Print the first n odd numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 3 5 7 9 11 13




# First n Square Numbers:
# You are given an integer n. Print the first n square numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 4 9 16 25 36 49





# Multiplication Table of n:
# You are given an integer n. Print the multiplication table of n till count 10.
# Sample Input: 
# 7
# Sample Output: 
# 7 14 21 28 35 42 49 56 63 70
# Explanation: Print 7*1, 7*2, …, 7*10.





# Factors of a Number:
# Write a program that takes a number n as input and prints all the factors of the number.
# Sample Input: 
# 24
# Sample Output: 
# 1 2 3 4 6 8 12 24
# Explanation: The factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24.





# Series: 3, 5, 7, 9, 11, …:
# You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…
# Sample Input: 
# 7
# Sample Output: 
# 3 5 7 9 11 13 15
# Explanation: The series starts with 3 and every time adds 2 to get the next term.





# Series: 2, 5, 8, 11, 14, …:
# You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…
# Sample Input: 
# 7
# Sample Output: 
# 2 5 8 11 14 17 20
# Explanation: The series starts with 2 and every time adds 3 to get the next term.





# Series: 3, 6, 12, 24, 48, …:
# You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
# Sample Input: 
# 7
# Sample Output: 
# 3 6 12 24 48 96 192
# Explanation: The series starts with 3 and every time multiplies 2 to get the next term.




# Sum of First n Natural Numbers:
# You are given an integer n. Print the sum of the first n Natural Numbers.
# Note: Use a loop instead of a mathematical formula.
# Sample Input: 
# 7
# Sample Output: 
# 28
# Explanation: Sum of 1+2+3+4+5+6+7 = 28





# Sum of Series: 3, 5, 7, 9, 11, …:
# You are given an integer n. Print the sum of the first n terms of the series 3, 5, 7, 9, 11….
# Note: Use a loop instead of a mathematical formula.
# Sample Input: 
# 7
# Sample Output: 
# 63
# Explanation: Sum of 3+5+7+9+11+13+15 = 63





# Factorial of a Number:
# Write a program to calculate the factorial of a given number n. 
# The factorial of a number n is the product of all positive integers less than or equal to n.
# Sample Input: 
# 6
# Sample Output: 
# 720
# Explanation: 720 = 6*5*4*3*2*1





# Counting Digits in a Number:
# Write a program that takes a number n as input and prints the number of digits the number has.
# Sample Input: 
# 1132
# Sample Output: 
# 4





# Sum of Digits of a Number:
# Write a program that calculates the sum of all the digits in a given number n.
# Sample Input: 
# 1132
# Sample Output: 
# 7
# Explanation: 7 = 1+1+3+2  
