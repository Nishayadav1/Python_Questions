# ------------------------sorting-----------------------

# 1. Bubble sort------------------------------------------
# Initial Pass: Start at the beginning of the list and compare the first two elements. 
# If the first element is greater than the second, swap them. 
# Then, move to the next pair of adjacent elements and repeat the process.


# l=[7,8,3,1,2]
# n=len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             a=l[j]
#             l[j]=l[j+1]
#             l[j+1]=a
# print(l)        




# selection sort------------------------------swap hota hai------
# --- Find the minimum element in the unsorted portion of the list.
# ----Swap it with the first element of the unsorted part.
# ---Repeat the process for the remaining unsorted elements.

# assending order
#  T & C=

# l=[7,8,3,1,2]   
# n=len(l)
# for i in range(n):
#     m=i 
#     for j in range(i+1,n):
#         if l[j]<l[m]:    # for discendibg order change arrow
#             m=j
#     l[i],l[m]=l[m],l[i]
# print(l)     


# insertion sort--------------------------------------
# Start with the second element (index 1) in the list and compare it with the first element.
# If the second element is smaller than the first, swap them.
# Move to the third element (index 2), compare it with the previous elements, and insert it in the correct position.
# Repeat the process for all elements until the entire list is sorted.

 
# l = [5, 2, 9, 1, 5, 6]
# n = len(l)
# for i in range(1, n):
#     k=l[i]
#     j=i-1
#     while j>=0 and l[j]>k:
#         l[j+1]=l[j]
#         j-=1
#     l[j+1]=k
# print(l)



# Qucik sort----------------------------------------
# Select a "pivot" element from the array.
# Partition the array such that elements less than the pivot are on its left and elements greater than the pivot are on its right.
# Recursively apply the same steps to the left and right subarrays until the array is fully sorted.






#marge sort--------------------------------------------    
#Divide: The list is recursively divided into two equal halves until each sublist contains a single element.
# Conquer: Recursively sort each of the two halves.
# Merge: Combine (merge) the two sorted halves into one sorted list. 

    