a = []
sum=0
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
    sum+=b
print(a)
average = sum/n
print("average of array is "+str(average))