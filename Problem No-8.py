# Write a recursive python function to print cubes of first N natural numbers.
def function(a):
    if a==1:
        print(1*1*1,end=" ")
    else:
        function(a-1)
        print(a*a*a,end=" ")
function(int(input("Enter the value of n to print cubes of first n natural numbers: ")))