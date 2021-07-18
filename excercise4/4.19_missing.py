# getMissingNo takes list as argument
def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A
 
 
# Driver program to test the above function
A = []
n = int(input("Enter Number of Elements in array:"))
for i in range(n):
    b= int(input())
    A.insert(i,b)
miss = getMissingNo(A)
print("missing number is"+str(miss))
# This code is contributed by Pratik Chhajer