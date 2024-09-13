'''Odd or Even:
# Write a program that takes a positive integer n as input and prints whether it is odd or even.
# Sample Input 1: 
# 49
# Sample Output 1: 
# Odd
# Sample Input 2: 
# 36
# Sample Output 2: 
# Even'''
# ---------------------------ans-----------------------------------
# num=int(input())
# if num%2==0:
#     print("even")
# else:
#     print("odd")    
    
 # --------------------------------------------------------------   
    
'''Grading System:
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
# '''
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
            
'''ge Group Categorizer
Write a program that categorizes a person's age into different life stages based on the following conditions:
0-2 years: Infant
3-12 years: Child
13-19 years: Teenager
20-65 years: Adult
Above 65 years: Senior
The program takes an age as input and prints the age group category the person belongs to. 
Sample Input 1:
15
Sample Output 1:
Teenager
Sample Input 2: 
2
Sample Output 2: 
Infant
Sample Input 3: 
72
Sample Output 3: 
Senior '''

# ---------------------------ans-----------------------------------
# age=int(input())
# if 0<age<=2:
#     print('Infant')
# elif 3<=age<=12:
#     print('child')   
# elif 13<=age<=19:
#     print('Teenager')
# elif 20<=age<=65:
#     print('child')   
# elif age>65:
#     print('Senior')     
        

# --------------------------------------------------------------


'''Temperature Adviser
Write a program that suggests an activity based on the current temperature (in Celsius), following these guidelines:
Above 30°C: "It's hot. Let's go swimming!"
20°C to 30°C: "Perfect for a picnic."
10°C to 19°C: "Maybe wear a jacket?"
Below 10°C: "Too cold! Best to stay indoors."
The program takes the current temperature as input and prints the suggested activity.
Sample Input 1: 
15
Sample Output 1: 
Maybe wear a jacket?
Sample Input 2: 
8
Sample Output 2: 
Too cold! Best to stay indoors.
Sample Input 3: 
38
Sample Output 3: 
It's hot. Let's go swimming! '''


# -----------------------ans---------------------------------------
# Tem_cel=int(input())
# if Tem_cel<10:
#     print('Too cold! Best to stay indoors.')
# elif 10<=Tem_cel<=19:
#     print('Maybe wear a jacket?') 
# elif 20<=Tem_cel<=30:
#     print("Perfect for a picnic.")    
# elif Tem_cel>30:
#     print("It's hot. Let's go swimming!")    

# --------------------------------------------------------------


''' Maximum of Three Numbers:
Write a program that takes three numbers as input and prints the largest number.
Sample Input 1: 
15 23 16
Sample Output 1: 
23
Sample Input 2: 
8 5 9
Sample Output 2: 
9 '''

# ------------------------ans--------------------------------------
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>n2 and n1>n3:
#     print(n1)
# elif n2>n1 and n2>n3:
#     print(n2)  
# else:
#     print(n3)   

# -------------------or--------------
# n1=int(input())
# n2=int(input())
# n3=int(input())
# m=max(n1,n2,n3)  
# print(m) 

# --------------------------------------------------------------


'''Sort Three Numbers
Write a program that takes three numbers as input and prints the numbers in ascending order.
This program doesn't use an array.
Sample Input 1: 
15 23 16
Sample Output 1: 
15 16 23
Sample Input 2: 
8 5 9
Sample Output 2: 
5 8 9 '''
# -----------------------ans---------------------------------------

# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1<n2 and n1<n3:
#     if n2<n3:
#         print(n1,n2,n3)
#     else:
#          print(n1,n3,n2)   
# elif n2<n1 and n2<n3:
#     if n1<n3:
#         print(n2,n1,n3)
#     else:
#          print(n2,n3,n1)  
# else:
#     if n1<n2:
#         print(n3,n1,n2)
#     else:
#          print(n3,n2,n1) 
