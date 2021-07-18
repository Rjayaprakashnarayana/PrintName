def diff_l_S(a,n):
    small=99999
    large =0
    for i in range(n):
        if(a[i]< small):
            small = a[i]
        if(a[i]>large):
            large = a[i]
    return large - small

arr = [] 
n = int(input("Enter Number of Elements in array:"))
for i in range(n):
    b= int(input())
    arr.insert(i,b) 
d = diff_l_S(arr ,n)
print("Difference between large value and small value is :"+str(d))