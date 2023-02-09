# accounts2anylenght.py
# Author: Norbert Antal
# weekly task: week03 extra:
# Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Modify the program to deal with account numbers of any length (comment your assumptions)

# prompt for account number
accno = (input("Please enter your account number: "))
#calculate last 4 digit by taking remainder of division by 10000 // and convert to string so len() can work
 ## last4 = str(accno % 10000)
#check lenght of original account number (source ref: https://www.geeksforgeeks.org/python-string-length-len/)
coverlenght = len(str(accno))-4
#combine account number lenght -4 X letters and last 4 digits of account number to conceal full account number 
 ## print(coverlenght * "X" + (last4))
accstr = str(accno)
#same but works with letters too (int related lines (11 and 15) muted)
print(coverlenght * "X" + accstr[(coverlenght)]+accstr[(coverlenght)+1]+accstr[(coverlenght)+2]+accstr[(coverlenght)+3])