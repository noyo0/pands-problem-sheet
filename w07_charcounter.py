# ecounter.py
# Author: Norbert Antal
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line. 
# count occurence ref: https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
# open with encoding spec ref: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# try error handling ref: https://www.w3schools.com/python/python_try_except.asp
# argparse ref: https://www.youtube.com/watch?v=cdblJqEUDNo
# argparse ref. https://docs.python.org/3/library/argparse.html
# Program reads in text file from same directory and loops through each caracter and increases counter by one if character in search variable matches with string item.

import argparse

#--------------CLA
parser = argparse.ArgumentParser(description="Count character occurances in text")
parser.add_argument("-f", "--file", type=str, required=True, help="filename with extension (mandatory)")
parser.add_argument("-c", "--char", type=str, required=False, default= "e", help= "a character (optional, default is \"e\")")
#parser.add_argument("-l", "--list", type=str, required=False, default="fn_list", help="scan directory for text files")
args = parser.parse_args()

#-------counter-function
def fn_ecounter(FILENAME="haiku1.txt",search="e"):
    count=0
    with open(FILENAME, "rt", encoding="utf8") as f:
        for data in f:
            text = data.strip()
            for t in text:
                if t == search:
                    count += 1
        print(f"\n{FILENAME} has {count} of \"{search}\" characters. \n Total number of characters: {len(text)}\n")

# ------------- list function
def fn_list():
    files = ["haiku1.txt","haiku2.txt","haiku3.txt"]
    print("\nPlease choose from:")
    for f in files:
        print(f)

#-------------call counter function with CLA or print file list if filename doesn't match-----------

try:
    fn_ecounter(args.file,args.char)
except:
    print("\n ERROR - Something didn't work out as planned")
    fn_list()


