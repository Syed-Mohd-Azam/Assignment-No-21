# Write a recursive python function to print first N odd natural numbers in reverse order.
def function(a):
    if a==1:
        print(2*a-1,end=" ")
    else:
        print(2*a-1,end=" ")
        function(a-1)
function(int(input("Enter the value of n to print first natural numbers in reverse order: ")))