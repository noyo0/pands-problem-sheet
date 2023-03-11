# w07_es_xt.py
# Author: Norbert Antal
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line. 
# count occurence ref: https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
# open with encoding spec ref: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# try error handling ref: https://www.w3schools.com/python/python_try_except.asp
# argparse ref: https://www.youtube.com/watch?v=cdblJqEUDNo
# argparse ref. https://docs.python.org/3/library/argparse.html
# os listdir ref: https://realpython.com/working-with-files-in-python/#:~:text=To%20get%20a%20list%20of,file%20size%20and%20modification%20date.
# Program reads in text file from "textfiles/" directory and loops through each caracter and increases counter by one if character in search variable matches with string item.

import argparse
import os
#--------------CLA
parser = argparse.ArgumentParser(description="Count character occurances in text")
parser.add_argument("-f", "--file", type=str, required=False, help="filename with extension (mandatory argument)")
parser.add_argument("-c", "--char", type=str, required=False, default= "e", help= "a character (optional, default is: e)")
args = parser.parse_args()

#-------counter-function
def fn_counter(FILENAME,SEARCH):
    count=0
    with open(f"textfiles/{FILENAME}", "rt", encoding="utf8") as f:
        for data in f:
            text = data.strip()
            for t in text:
                if t == SEARCH:
                    count += 1
        print(f"\n{FILENAME} has {count} counts of \"{SEARCH}\" characters.\n")

# ------------- file list function
def fn_list():
    filelst=os.scandir('textfiles/')
    for f in filelst:
        print(f)
        

#-------------call counter function with CLA or print file list if filename doesn't match-----------

try:
    fn_counter(args.file,args.char)
except:
    print("""\nERROR - Something didn't work out as planned.\n
    Please use arguments:
  -f, filename with extension (mandatory argument)
  -c, a character to count (optional, default is: e)
    \nCurrently available text files: \n""")
    fn_list()


