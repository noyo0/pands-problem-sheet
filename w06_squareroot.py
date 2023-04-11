# squareroot.py
# Author: Norbert Antal
# Program finds approximate square root of a given number with Newton-Raphson Method
# Created function "fn_newton" with two arguments; number, display. 
# "number" argument sets the number to calculate with, 
# "display" argument determines if the result is displayed as integer (default:0) or a floating point number (1)
# Program runs until max accuracy is reached;
    # I noticed that while allowing infinite iterations of the square root calculation, python limits the number of digits at 17 so the results are repeating once 17-digit accuracy is achieved.
    # Exploiting this "feature" the program can store results in a container and check current result against previous iteration. 
    # If the two are the same, the result must be the most accurate within this 17-digit restriction and the program can break out of the loop as there is no need to iterate any more.
# ref: Newton-Raphson Formula: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# ref: 17 digit rounding: https://docs.python.org/3/tutorial/floatingpoint.html


''' # -------fn_newton------------------------start

def fn_newton(number,disp=0):
    i=0
    itr=100 #maximum number of iterations in case of extreme large numbers (probably overkill)
    x=number #starting number as per user input
    result=[] # result container to find the most accurate approximation
    while i<itr:
        x=0.5*(x+number/x) # Calculating the Square Root of a Number using the Newton-Raphson Method
        i+=1 # increase iteration counter by 1
        if x not in result: # checks if results are repeating
            result.append(x) # if not, stores result in the result container "res[]" and continues with the loop
        else:# if result equals stored result from previous iteration, the current result is the most accurate, the program continues to the return function
            if disp==1: #check if user defined result display method (int or float)
                return(int(x)) # if user chose int, result returns as int
            else:
                return(x)  # if user chose float (or left the second argument blank), result returns as float
            
# -------fn_newton------------------------end'''

# ☝️AFTER FEEDBACK 
# - eliminate limited iteration from while loop, 
# - improve output with the introduction of user defined rounding,
# - give more meaningful variable names

# -------fn_newton------------------------start
def fn_newton(number,roundto=0):
    x=number #starting number as per user input
    result=[] # result container to find the most accurate approximation
    while x != result:
        x=round(0.5*(x+number/x),roundto) # Calculating the Square Root of a Number using the Newton-Raphson Method + rounding to 
        if x not in result: # checks if results are repeating
            result.append(x) # if not, stores result in the result container "res[]" and continues with the loop
        else:
            return(x)       
# -------fn_newton------------------------end

# user interaction ---------
# enter number
number=float(input("Please enter a positive floating-point number: ")) # user prompted for a positive floating point number
while number<=0: # program will wex the user until positive number is given
    number=float(input("...please enter a positive floating-point number: ")) 
# enter rounding
roundto=int(input("How many digits to round to? ")) # User prompted for display method
# call function
sqrroot=fn_newton(number,roundto) # setting value for "p" by calling function fn_newton with arguments defined by user interaction
#output square root result
print(f"\n\n The square root of {number} is approximately: {sqrroot}") #starting number and approximate square root is printed as per user interaction
