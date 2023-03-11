# w07_es.py
# Author: Norbert Antal
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line. 
# Strip ref: https://www.w3schools.com/python/ref_string_strip.asp#:~:text=The%20strip()%20method%20removes,default%20leading%20character%20to%20remove)
# count occurence ref: https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
# Command line Arguments with sys module ref: https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv#:~:text=argv%3F-,sys


import sys

FILENAME = sys.argv[1]
count = 0
with open(FILENAME, "rt") as f:
        for data in f:
            text = data.strip()
            for t in text:
                if t == "e":
                    count += 1
        print(count)