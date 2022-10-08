# Write a recursive python function to print first N natural numbers.
def function(a):
    if a==1:
        print(1,end=' ')
    else:
       function(a-1)
       print(a,end=" ")
function(int(input("Enter the value of n to print first n natural numbers : ")))