# accounts.py
# Author: Norbert Antal
# weekly task: week03:
# Program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# prompt for account number
accno = int(input("Please enter your 10 digit account number: "))
#calculate last 4 digit by taking remainder of division by 10000
last4 = str(accno % 10000)
#combine 6X and last 4 digits to conceal full account number 
print(f"XXXXXX{last4}")