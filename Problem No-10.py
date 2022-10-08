#  Write a recursive python function to print a number in reverse order.
def function(a):
    if a<=0:
        return(1)
    else:
        print(int(a%10),end="")
        function(int(a/10))
function(int(input("Enter a number to print in reverse order: ")))