# squareroot.py
# Author: Norbert Antal
# Program finds square root of a given number with Newton's method
# Utilising function with two arguments. First argument sets the number to calculate with, the second argument determines if the result is displayed as floating point number (0-default) or an integer (1)
# Program runs until max accuracy is achieved. This is achieved by exploiting the python's apparent 17 digit floating point limitation by comparing results with previously stored results, if the new result is the same as the previous one the program would only repeat the same number so no point iterating any more and store the result as final.
# ref: Newton's method: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# ------------------------------fn_newton-------start--------
def fn_newton(number,float=0,acc=10):
    i=0
    itr=100 #maximum number of iterations
    x=number
    res=[] # result container
    while i<itr:
        x=round((x+number/x)/2,acc) # Calculating the Square Root of a Number using the  Newton-Raphson Method
        i+=1
        if x not in res: # checks if result is repeating (after reaching max accuracy the results repeating)
            res.append(x) # if not, adds stores it in the result container acc[]
            print(x)
        else:
            print(res)
            if float==1: #check if user defined result display method (int or float)
                return(int(x)) # if user chose int, result returns as int
            else:
                return(x)  # if user chose float (or left the second argument blank), result returns as float
# -----------------------------fn_newton---------end-----------

print("""
Square root function called fn_newton() takes 3 arguments fn_newton(number, display, accuracy)
    - number - is a positive floating point number to find the square root for
    - display - determines if the result is displayed as an integer or a floating point number
    - accuracy - sets the accuracy between 1-17 digits""")
n=float(input("Please enter a positive floating-point number: ")) # user prompted for a positive floating point number
while n<=0: # program will wex the user until positive number is given
    n=float(input("...but seriously, please enter a positive floating-point number: ")) 
acc=int(input("Default accuracy is 10 digits or enter a new number between 1-17: "))
while acc not in range(1,18):
    acc=int(input("a number between 1-17 please: "))
f=str(input("Do you want the result as a floating point(Yes?): ")) # User prompted for display method
if f== "Y" or f=="y" or f=="yes" or f=="Yes": # Program allows for few types of "yes" entries for Floating point display, everything else results in integer display
    f=0
else:
    f=1
p=fn_newton(n,f,acc) # setting variable p for printing the result
print(f"\n\nthe square root of {n} is approximately: {p}") #result is printed as per user interaction
