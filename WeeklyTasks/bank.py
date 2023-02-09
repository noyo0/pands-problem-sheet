# bank.py
# weekly tasks: week02
# Author: Norbert Antal
# Program functions:
#   Prompt the user and read in two money amounts (in cent)
#   Add the two amounts
#   Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
amount1 = int(input("Enter the first amount (in cents):\t "))
amount2 = int(input("Enter the second amount (in cents):\t "))
eur = (amount1+amount2)/100
print(f"The sum of these is: \t\t\t€{eur}")