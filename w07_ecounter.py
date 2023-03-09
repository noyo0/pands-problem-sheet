# ecounter.py
# Author: Norbert Antal
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line. 
# count occurence ref: https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
# open with encoding spec ref: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# CLA ref: https://www.youtube.com/watch?v=QJBVjBq4c7E
# try error handling ref: https://www.w3schools.com/python/python_try_except.asp
# Program reads in text file from same directory and loops through each caracter and increases counter by one if character in search variable matches with string item.

import sys 

def fn_ecounter(FILENAME="haiku1.txt",search="e"):
    count=0
    with open(FILENAME, "rt", encoding="utf8") as f:
        for data in f:
            text = data.strip()
            for t in text:
                if t == search:
                    count += 1
        print(f"{FILENAME} has {count} of \"{search}\" characters. \n Total number of characters: {len(text)}")
try:
    fn_ecounter(sys.argv[1],sys.argv[2])
except:
    fn_ecounter()