# Write a recursive python function to print squares of first N natural numbers.
def function(a):
    if a==1:
        print(1*1,end=" ")
    else:
        function(a-1)
        print(a*a,end=" ")
function(int(input("Enter the value of n to print squares of first n natural numbers: ")))