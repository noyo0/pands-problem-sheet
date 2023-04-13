# collatz.py
# Author: Norbert Antal
# weekly task: week04:
# Program asks the user to input any positive integer and outputs the successive values of the following calculation;
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Program ends if the current value is one.

number = int(input("Please enter a positive integer: "))
# creating list to store each value of var(number) per iteration
numbers = [str(number)] # convert integer to string to store in list (list item data types - ref: https://www.w3schools.com/python/python_lists.asp)
# create loop to repeat until var(number) equals 1
while number > 1:
    # check if number is even and divide with two if True
    if (number % 2) == 0:
        number = int(number//2)
    #otherwise multiply with 3 and add 1
    else:
        number = number*3+1
    # convert to string and add result to list[numbers]
    numbers.append(number)
# print items of list[numbers] with space as divider
print('your result:')
print(*numbers) # (print with custom dividers - ref: https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row)

# ☝️RE: FEEDBACK
# my feedback was: Task04 Collatz:
'''Some people did not pay attention to the requested output, for you:
good, but this puts commas between the numbers, can you do it without the commas'''

# I couldn't replicate the issue. 
# By using print with a star in front 'print(*numbers)' the result is showing without commas. 
# tested in VSC and cmd Terminal

# example from cmd Terminal:
# C:\Users\norbe\OneDrive\ATU_Galway\pands\pands-problem-sheet (main -> origin)
'''
λ python w04_collatz.py
Please enter a positive integer: 5
your result:
5 16 8 4 2 1



'''

