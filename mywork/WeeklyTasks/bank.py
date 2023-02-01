# bank.py
# weekly tasks: week02
# Author: Norbert Antal
#   When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
#   Write a program called bank.py 
#   The program should:
#   Prompt the user and read in two money amounts (in cent)
#   Add the two amounts
#   Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#   $ python bank.py
#   Enter amount1(in cent): 65
#   Enter amount2(in cent): 180
#   The sum of these is €2.45
amount1 = int(input("Enter the first amount (in cents):\t"))
amount2 = int(input("Enter the second amount (in cents):\t"))
eur = (amount1+amount2)/100
print(f"The sum of these is: \t\t\t€{eur}")
