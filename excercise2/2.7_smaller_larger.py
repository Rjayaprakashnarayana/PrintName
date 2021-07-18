b=[0,0,0,0,0,0,0,0]
small =9999
large =0
n= int(input("Enter The number of numbers to be added:"))
for i in range(n):
    b[i]=int(input())
    if(b[i]<small):
        small = b[i]
    if(b[i]>large):
        large =b[i]
print("smaller number in list : "+str(small))
print("larger number in list : "+str(large))
