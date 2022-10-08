# Write a recursive python function to print first N even natural numbers.
def function(a):
    if a==1:
        print(2*1,end=" ")
    else:
        function(a-1)
        print(2*a,end=" ")
function(int(input("Enter the value of n to print first n even natural numbers: ")))