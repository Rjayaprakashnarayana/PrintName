
# Python program to 
# find second largest  
# element in an array 
  
  
# Function to print the 
# second largest elements  
def print2largest(arr,arr_size): 
  
    # There should be atleast 
        # two elements  
    if (arr_size < 2): 
      
        print(" Invalid Input ") 
        return
      
  
    first = second = -2147483648
    for i in range(arr_size): 
      
        # If current element is 
                # smaller than first 
        # then update both 
                # first and second  
        if (arr[i] > first): 
          
            second = first 
            first = arr[i] 
          
  
        # If arr[i] is in 
                # between first and  
        # second then update second  
        elif (arr[i] > second and arr[i] != first): 
            second = arr[i] 
      
    if (second == -2147483648): 
        print("There is no second largest element") 
    else: 
        print("The second largest element is", second) 
  
  
# Driver program to test 
# above function  
arr = [] 
n = int(input("Enter Number of Elements in array:"))
for i in range(n):
    b= int(input())
    arr.insert(i,b) 
print2largest(arr, n)