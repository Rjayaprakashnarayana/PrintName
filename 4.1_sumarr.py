def sum1(a,n):
    sum=0
    for i in range(n):
        sum+=a[i]
    return sum

a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print(sum1(a,n))