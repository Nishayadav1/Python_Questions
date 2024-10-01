# ---------------linear search
# t&C == n worst case

# l=[1,4,2,7,5,8]
# t=8 
# for i in range(len(l)):
#     if t==l[i]:
#         print(i)
#         break
    
    
    
# ---------------binary search   
# T & C  == Log(n)d

l=[9,3,5,7,1,4,0]
l.sort()
# print(l)
t=4
n=len(l)-1
i=0
while i<=n:
    m=(i+n)//2
    if t<l[m]:
        n=m-1
    elif t>l[m]:
        i=m+1
    else:
        print("yes")
        break
else:
    print("-1")         
        
    
    
