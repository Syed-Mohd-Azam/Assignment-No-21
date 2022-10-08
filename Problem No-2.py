# Write a recursive python function to print first N natural numbers in reverse order.
def function(a):
    if a==1:
        print(1,end=" ")
    else:
        print(a,end=" ")
        function(a-1)
function(int(input("Enter the value of n to print first n natural numbers in reverse order! ")))