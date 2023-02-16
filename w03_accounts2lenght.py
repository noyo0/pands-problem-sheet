# accounts2anylenght.py
# Author: Norbert Antal
# weekly task: week03 extra:
# Program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Modified program to deal with text input of any lenght and allow letters

# prompt for account number
accno = (input("Please enter whatever you want: "))
#check lenght of original account number (source ref: https://www.geeksforgeeks.org/python-string-length-len/) and take 4 to get the number of "X" we need to cover the concealed part of the account number
coverlenght = len(str(accno))-4
#convert accno to string
accstr = str(accno)
#display an amount of "X" equal to acc number lenght minus 4 and select last 4 characters from account number as string (this allows for letters in the account number) to display last 4 digits/characters
print(coverlenght * "X" + accstr[(coverlenght):(coverlenght)+4]) #found a nicer slicer (source ref: https://www.interviewqs.com/ddi-code-snippets/substring-python)