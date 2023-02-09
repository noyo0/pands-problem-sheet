# accounts2anylenght.py
# Author: Norbert Antal
# weekly task: week03 extra:
# Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Modify the program to deal with account numbers of any length (comment your assumptions)
# same but works with letters too

# prompt for account number
accno = (input("Please enter whatever you want: "))
#check lenght of original account number (source ref: https://www.geeksforgeeks.org/python-string-length-len/) and take 4 to get the number of "X" we need to cover the concealed part of the account number
coverlenght = len(str(accno))-4
#convert accno to string
accstr = str(accno)
#display an amount of "X" equal to acc number lenght minus 4 and select last 4 characters from account number as string (this allows for letters in the account number) to display last 4 digits/characters
print(coverlenght * "X" + accstr[(coverlenght):(coverlenght)+4]) #found a nicer slicer (source ref: https://www.interviewqs.com/ddi-code-snippets/substring-python)
