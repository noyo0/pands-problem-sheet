## ATU-Galway - Programming and Scripting
### Author: Norbert Antal
#### **pands-problem-sheet**
###### This "pands-problem-sheet" folder contains solutions and documentation for the weekly tasks.

---

## Contents:
- Week01: Hello World
- Week02: Bank
- Week03: Accounts
- Week04: Collatz
- Week05: Weekday
- Week06: Square root
<br>

>
>
---
---
<br>

## Week01: Hello World
> w01_helloworld.py  

    Weekly Task Description:
    "Commit and push a file to the problem sheet called helloworld.py"

Program displays "Hello World!"

---
---
<br>

## Week02: Bank
> w02_bank.py
 
    Weekly Task Description:
    "Write a program called bank.py 
    The program should: 
    - Prompt the user and read in two money amounts (in cent)
    - Add the two amounts
    - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount"

Program prompts the user to type in two money amounts in cents and stores them in 2 variables "amount1" and "amount2". The program adds the two values together and divides the sum by 100 thus converting the cent values to euro and outputs the answer with a euro sign and decimal point between the euro and cent of the amount.

---
---
<br>

## Week03: Accounts
> w03_waccounts.py

    Weekly Task Description:
    "Write a python program called accounts.py that reads in
    a 10 character account number and outputs the account number
    with only the last 4 digits showing 
    (and the first 6 digits replaced with Xs)."

Program promts user for a 10 digit account number, then devides the number by 10,000 to get the last 4 digits with a modulo operator and stores the value in a variable. Program than prints out 6 "X"characrters followed by the 4 digits stored in the variable.
>
 - ### Week03: Extra 
> w03_accounts2lenght.py
 
    Weekly Task Description Extra: 
    "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"

The modified program promts user for a 10 digit account number, then checks lenght of the given number using the len function (*Reference 1.*) and deducts 4 to establish how many characters of the accoun t number must be replaced with "X". The result is then stored in variable "coverlenght". The program then converts the original number to string and stores it in variable "accstr" so it can be concatenated and its individual characters can be called between a range (*Reference 2.*). Finally the program concatenates as many "X" caracters as the value stored in coverlenght and calls the last 4 digits from "accstr" by referring to the range from position that equals coverlenght to position that equals coverlenght + 4.
Since the user entry is stored and manipulated as string, there is no limitations to numbers only, the program can deal with any character.
- ##### *References:*
##### *1. len function (https://www.geeksforgeeks.org/python-string-length-len/)*
##### *2. find certain section of a string (https://www.interviewqs.com/ddi-code-snippets/substring-python)*
---
---
<br>

## Week04: Collatz
> w04_collatz.py

    Weekly Task Description:
    "Write a program, called collatz.py, that asks the user to input any positive integer 
    and outputs the successive values of the following calculation. At each step calculate
    the next value by taking the current value and, if it is even, divide it by two, 
    but if it is odd, multiply it by three and add one.
    Have the program end if the current value is one.
    Example of it running:
    $ python collatz.py
    Please enter a positive integer: 10
    10 5 16 8 4 2 1"

 Program asks user to input any positive integer which is stored as integer in variable "number". A list "numbers[]" is created where each result of the calculation will be stored (*Reference 1.*). <br> The formula to get each member of a Collatz sequence was provided in the Weekly Task Description. The program assumes the endpoint of a Collatz seqence is always positive 1 /until someone proves otherwise/ (*Reference 3. and 4.*) so a while loop is initiated which breaks when the value of "number" reaches 1. <br>Whithin the while loop an if statement assigns the appropriate calculations to odd and even numbers based on their divisibility with 2 with 0 remiander using a modulus operator.<br> The result of each itearations updates the variable "number" than stored in list "numbers[]" (*Reference 1.*). Once the value of "number" reaches 1, the loop is ended and the values stored in "numbers" are printed with formatting that prints each item side by side with space as divider (*Reference 2.*) as per example in the task description.
-    ##### *References:* 
##### *1. list item data types - ref: (https://www.w3schools.com/python/python_lists.asp)*
##### *2. print with custom dividers - ref: (https://stackoverflow.com/questions/11178061/pint-list-without-brackets-in-a-single-row)*
##### *3. Collatz conjencture - ref: (https://en.wikipedia.org/wiki/Collatz_conjecture)*
##### *4. The Simplest Math Problem No One Can Solve - Collatz Conjecture - ref: (https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s)*
---
---
<br>

## Week05: Weekday
> w05_weekday.py

    Weekly Task Description:
    "Write a program that outputs whether or not today is a weekday."

Program checks if current date falls on a weekday or not, using the imported -datetime- module's date.weekday() function that returns the day of the week as an integer, where Monday is 0 and Sunday is 6. (*Reference 1.*)<br> 
An if statement determines wether the current day represented as integer is a weekend day (larger than 4) otherwise it must be a weekday. Based on the if statement the appropriate message is printed.
There is no user interaction in this program.
##### - *References:* 
##### *1. datetime module - (https://docs.python.org/3/library/datetime.html)*
---
---
<br>

## Week06: Square root
> w06_squareroot.py

    Weekly Task Description:
    "Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called <tt>sqrt</tt> that does this. I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots.

Program is separated into two parts;<br> **First part** is defining the square root function "fn_newton" to find a close approximate for square root of a given number with Newton-Raphson Method (*Reference 1.*) <br> The function "fn_newton" has 2 arguments;<br> "number" for storing the starting number from user interaction later and <br> "display" argument that determines if the result is displayed as floating point number (default:0) or as an integer (1) <br>
The function starts with setting up values for the iterators, "i" is the iterator and "itr" is the maximum number of iterations. Also giving the value of "number" for "x" for the first iteration of the "x=0.5*(x+number/x)" formula (*Reference 2.*).<br> 
Initially planned to iterate the calculation a set number of times and see what gives the best approximation but noticed that while allowing infinite iterations for the square root calculation, Python limits the number of digits at 17 so the results are repeating once 17-digit accuracy is achieved.<br> I found this number representation issue mentioned in reference to older versions of Python (*Reference 2.*).
Exploiting this "feature" so to speak, I created a container for the results "res[]" so the program can store results in a list and check current result against the result from the previous iteration. <br> Once current result and previous iteration are the same, the result must be the most accurate within this 17-digit restriction and the program can break out of the loop as there is no need to iterate any more. 
As a failsafe in case for extreme large numbers I left the max iteration variable in the function with value set to 100. This may be an unnecesary precaution, I could count a few iterations with extra large numbers and settle for a smaller number but didn't want to spen dmore time.<br>
The **second part** of the program is user interaction which provides the starting number where the Program insists on a positive number if negative is given, and user also choses if the result is printed as integer or floating point number. <br>
- **Notes:**
<br>
By rounding the calculation to a smaller number than 17, thus reducing accuracy, the return of the result can be quicker. To avoid "feature creep", I ultimately removed this function. I left "display" argument only to demonstrate default values in function arguments.

- ##### *References:*
##### *1. Newton-Raphson Method: (https://en.wikipedia.org/wiki/Newton%27s_method)*
##### *2. Newton-Raphson Formula: (https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)*
##### *3. Floating Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html*
---
---
<br>

## Week07: Character counter
###  Simple version
> w07_es.py
    
    Weekly Task Description:
    "Write a program that reads in a text file and outputs the number of e's it contains.
    The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up."    
    
- *Program assumes the user already knows that moby-dick.txt must be given as argument.*

Program reads in a text file with filename passed from argument on command line to "FILENAME" variable using the imported **sys module** (ref 1. and 2.). File is read in as "f" using the with method as discussed in week 7 lecture.<br> A for loop reads in each line of the text stored in "f" as "data". Text in "data" is formatted by stripping leading and trailing characters (ref 3.), the result is stored in variable "text". Another for loop cycles throuhg each character storing current character in "t". An if statement checks if the current character in "t" variable is a character **e**, if so, variable "count" is increased by one (ref 4.). When the loop finished, the accumulated value of "count" is printed.<br>
***Limitations:*** Program only works with text file **moby-dick.txt** located in the same directory and only looks for the character **"e"**.

##### - *References:* 
##### *1. Command line Arguments with sys module ref: (https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv#:~:text=argv%3F-,sys)*
##### *2. CLA with sys ref: (https://www.youtube.com/watch?v=QJBVjBq4c7E)*
##### *3. strip method ref: (https://www.w3schools.com/python/ref_string_strip.asp#:~:text=The%20strip()%20method%20removes,default%20leading%20character%20to%20remove)*
##### *4. count occurence ref: (https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/)*
<br>

### Extended version
> w07_es_xt.py

- Extended version assumes the user starts the program unaware that arguments must be given. The programs features extended so it works with any of the files stored in specific folder "textfiles" and the user can chose any character while default is "e".

Command Line Arguments configured using **argparse** instead of sys. (ref 1. and 2.)are passing 2 arguments to a function "fn_counter" <br>
**Command Line Argumnents are:**<br>
**-f** for a filename to read in. This is passed to the "FILENAME" argument in function "fn_counter"<br>
**-c** for a character to count. This is passed to the "SEARCH" argument in "fn_counter" with default value "e".<br>
Program calls function "fn_counter" that carries out the task of reading in the text file given in the Command line argument as -f and counts the character given as second argument as -c while default is "e".<br> The textfile is read in as UTF-8 to deal with the read errors I encounterd. (ref 3.)
<br>When the loop finished the results are printed including file name, character count and character selected.<br>
**Error Handling**:
Program runs a try / except (ref 3.) error handling to deal with running with no arguments or with filenames that are not in the folder. This includes a function "fn_list" that is listing all files in "textfiles" directory using the imported os module's os.scandir() function (ref 5.). <br>
at "try" the programm calls "fn_counter" with arguments passed from command line<br>
at "except" the program instruct user regarding arguents and provides list of availbale text files stored in "textfiles" folder


##### - *References:* 
##### *1. argparse ref: (https://www.youtube.com/watch?v=cdblJqEUDNo)*
##### *2. argparse ref. (https://docs.python.org/3/library/argparse.html)*
#####  Count occurence ref: (https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/)
##### *3. Open textfile with encoding specified ref: (https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character)
##### *4. error handling "try/except" ref: (https://www.w3schools.com/python/python_try_except.asp)*
##### *5 os.scnadir() ref: (https://docs.python.org/3/library/os.html#os.scandir)*
##### *6 line split ref: (https://www.youtube.com/watch?v=oAFkPMbwRVY&t=214s)*
---
---
<br>