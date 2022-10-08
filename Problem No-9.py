# Write a recursive python function to print first N multiples of a given number.
def function(num,n):
    if n==1:
        print(num*1,end=" ")
    else:
        function(num,n-1)
        print(num*n,end=" ")
number,N=int(input("Enter a number : ")),int(input("Enter how many multiples you want : "))
function(number,N)