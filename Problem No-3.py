# Write a recursive python function to print first N odd natural numbers.
def function(a):
    if a==1:
        print(2*a-1,end=" ")
    else:
        function(a-1)
        print(2*a-1,end=" ")
function(int(input("Enter the value of n to print first n odd natural numbers! ")))