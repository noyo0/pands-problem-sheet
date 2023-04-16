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
- Week07: Character counter
- Week08: Plotting
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

Program displays "Hello World!" Using the print() function.


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

Program prompts the user to type in two money amounts in cents and stores them in 2 variables "amount1" and "amount2". The program adds the two values together and divides the sum by 100 thus converting the cent values to euro and outputs the answer euros and cents.

<br>☝️Feedback was: 
*The real test of this was can you do this without using floats (even hidden floats, e.g. /100) for you:
This is fine, though I would like the solution to be formatted and it would be ideal is you did not use floats (/100)*

#### 🤞After correction: 
Instead of a simple division (/100) that produced a floating point number stored in 'eur', the program uses a Floor division (// 100) that returns the nearest whole number to get the euro amount and a Modulus (% 100) to get the remainder of the division for the cent amounts. Both stored in their respective variables aptly named 'euro' and 'cent'. 
The output then formatted so the starting values, their sum in cents and the converted amount is displayed in one sentence.

- ###### *References:*

###### *1. Integer and float division ref: https://www.educative.io/answers/what-is-integer-and-float-division-in-python*

---
---
<br>

## Week03: Accounts
> w03_accounts.py

    Weekly Task Description:
    "Write a python program called accounts.py that reads in
    a 10 character account number and outputs the account number
    with only the last 4 digits showing 
    (and the first 6 digits replaced with Xs).
    **Weekly Task Description Extra: **
    "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"

The program promts user for a 10 digit account number, then checks lenght of the given number using the len function (*Reference 1.*) and deducts 4 to establish how many characters of the account number must be replaced with 'X'. The result is then stored in variable 'coverlenght'. The program then converts the original number to string and stores it in variable 'accstr' so it can be concatenated and its individual characters can be sliced between a range (*Reference 2.*). 
Finally the program concatenates as many 'X' caracters as the value stored in 'coverlenght' and calls the last 4 digits from 'accstr' by referring to the range from position that equals coverlenght to position that equals coverlenght + 4.
Since the user entry is stored and manipulated as string, there is no limitations to numbers only, the program can deal with any character.
- ##### *References:*
##### *1. len function (https://www.geeksforgeeks.org/python-string-length-len/)*
##### *2. find certain section of a string (https://www.interviewqs.com/ddi-code-snippets/substring-python)* 
<br>

☝️Feedback was: 
*There is a much simpler way of doing this with string splicing (ok I see you put that in aother file)*

#### 🤞I hope that means A-okay. Redundant file removed.
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

 Program asks user to input any positive integer which is stored as integer in variable "number". A list "numbers[]" is created where each result of the calculation will be stored starting with the initial number from user input(*Reference 1.*). <br> The formula to get each member of a Collatz sequence was provided in the Weekly Task Description. The program assumes the endpoint of a Collatz seqence is always positive 1 /until someone proves otherwise/ (*Reference 3. and 4.*) so a while loop is initiated which breaks when the value of "number" reaches 1. <br>Whithin the while loop an if statement assigns the appropriate calculations to odd and even numbers based on their divisibility with 2 with 0 remiander using a modulus operator.<br> The result of each iterations updates the variable "number" than stored in list "numbers[]" (*Reference 1.*). Once the value of "number" reaches 1, the loop is ended and the values stored in "numbers" are printed with formatting that prints each item side by side with space as divider (*Reference 2.*) as per example in the task description.
-    ##### *References:* 
##### *1. list item data types - ref: (https://www.w3schools.com/python/python_lists.asp)*
##### *2. print with custom dividers - ref: (https://stackoverflow.com/questions/11178061/pint-list-without-brackets-in-a-single-row)*
##### *3. Collatz conjencture - ref: (https://en.wikipedia.org/wiki/Collatz_conjecture)*
##### *4. The Simplest Math Problem No One Can Solve - Collatz Conjecture - ref: (https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s)*<br>
<br>


☝️Feedback was: 
*Some people did not pay attention to the requested output, for you: good, but this puts commas between the numbers, can you do it without the commas* 


#### 🤞I was unable to replicate the issue, result does show without commas.
By using print with a star in front of the variable <print(*numbers)> the result is showing without commas.<br>
Tested in VSC and cmd Terminal, result was without commas in both cases.


+ *Copy/Paste example from cmd Terminal:*<br>
C:\Users\norbe\OneDrive\ATU_Galway\pands\pands-problem-sheet (main -> origin)<br>
λ python w04_collatz.py<br>
Please enter a positive integer: 5<br>
your result:<br>
5 16 8 4 2 1

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

☝️There was no feedback on this one

---
---
<br>

## Week06: Square root
> w06_squareroot.py

    Weekly Task Description:
    "Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called <tt>sqrt</tt> that does this. I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots.

Program is separated into two parts;<br><br> **First part** is defining the square root function "fn_newton" to find a close approximate for square root of a given number with Newton-Raphson Method (*Reference 1.*) <br>The function "fn_newton" has 2 arguments;<br> "number" for storing the starting number from user interaction later and <br>
"roundto" argument that determines the number of digits displayed in the result<br>
The function starts with giving the value of "number" as the user defined starting point for "x" for the first iteration of the "x=0.5*(x+number/x)" formula applying the Newton-Raphson Method (*Reference 2.*) in a while loop.<br>
Initially planned to iterate the calculation a set number of times and see what gives the best approximation but noticed that while allowing infinite iterations for the square root calculation, Python limits the number of digits at 17 so the results are repeating once 17-digit accuracy is achieved.<br> I found this number representation issue mentioned in reference to older versions of Python as well (*Reference 3.*).<br>
Exploiting this 'feature' so to speak, I created a container for the results "prevresult[]" so the program can store results in a list and check current result against the result from the previous iteration. <br>
Once current result and previous iteration are the same, the result must be the most accurate within this 17-digit restriction. Hence the condition of the while loop is set to be true until current calculation result (x) and the last item in previous result (prevresult[]) is equal. Once they are the same, the calculation reached its max accuracy and current result (x) is retuned for the function.<br>
As a secondary function, the Newton-Raphson Method formula is encapsulated in a round() function, fich is determined by the value from the second (optional) argument of the fn:newton() function that has the default value of 0.
<br>
The **second part** of the program is user interaction which provides the starting number where the program insists on a positive number to be given, and user also choses rounding accuracy.  <br>
<br>
- ##### *References:*
##### *1. Newton-Raphson Method: (https://en.wikipedia.org/wiki/Newton%27s_method)*
##### *2. Newton-Raphson Formula: (https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)*
##### *3. Floating Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html*

<br>☝️Feedback was: 
*In this task I was asking you to write your own function that took in a number and returned a value, for you:
Good, though you do this for a specific number of iterations. Try to use more meaningfull variable names.*

#### 🤞After correction:
- eliminated limited iteration from while loop by using the container for previous results (prevresults[]) in the while loop instead of a separate iterator variable. **While** is true if current result and previous result is not equal. Once they are the same, the calculation reached its max accuracy and current result (x) is retuned for the function.
- improved output with the introduction of user defined rounding variable
- given more meaningful variable names
---
---
<br>

## Week07: Character counter
###  Simple version
> w07_es.py
    
    Weekly Task Description:
    "Write a program that reads in a text file and outputs the number of e's it contains.
    The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up."    

- Program assumes the user is unaware that arguments must be given. The programs handles any of the text files stored in a specific folder "textfiles" and the user can chose any character while default is "e".
- If the program executed without arguments, an error message outlines what arguments are available and a list of text files to chose from.

Command Line Arguments configured using **argparse**. (*Reference 1. and 2.*) are passing 2 arguments to a function "fn_counter" <br>
**Command Line Argumnents are:**<br>
**-f** for a filename to read in. This is passed to the "FILENAME" argument in function "fn_counter"<br>
**-c** for a character to count. This is passed to the "SEARCH" argument in "fn_counter" with default value "e".<br>
Program calls function "fn_counter" that carries out the task of reading in the text file given in the Command line argument as -f and counts the character given as second argument as -c while default is "e".(*Reference 3.*)<br> The textfile is read in as UTF-8 to deal with the read errors I encounterd. (*Reference 4.*)
<br>When the loop finished the results are printed including file name, character count and character selected.<br>
**Error Handling**:
Program utilises a try / except error handling method(*Reference 5.*) to deal with running with no arguments or with filenames that are not in the folder. As part of the error handling a second function "fn_list" was created that is listing all files in "textfiles" directory using the imported os module's os.scandir() function (*Reference 6.*).<br>
At "try" the programm calls "fn_counter" with arguments passed from command line<br>
At "except" the program instruct user regarding arguments and provides list of availbale text files stored in "textfiles" folder calling the fn_list() function.

- ###### *References:* 
###### *1. argparse ref: (https://www.youtube.com/watch?v=cdblJqEUDNo)*
###### *2. argparse ref. (https://docs.python.org/3/library/argparse.html)*
###### *3 Count occurence ref: (https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/)
###### *4. Open textfile with encoding specified ref: (https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character)
###### *5. error handling "try/except" ref: (https://www.w3schools.com/python/python_try_except.asp)*
###### *6 os.scnadir() ref: (https://docs.python.org/3/library/os.html#os.scandir)*
###### *7 line split ref: (https://www.youtube.com/watch?v=oAFkPMbwRVY&t=214s)*

<br>☝️Feedback was: 
*The specification for this task is a bit vague, I wanted to see what assumptions you made for this, for you:
good, though I would suggest having the letter looked for as a vairable, so that the code can be easily reused for other letters, you program will crach if no argument is passed*

#### 🤞I had two versions uploaded and the more simplistic first version was reviewed the extended version was not.<br> Removed redundant first version and updated readme file.

---
---
<br>

### Week08: Plotting
> w08_plottask.py

    Weekly Task Description:
    "Write a program called plottask.py that displays:
        - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
        - and a plot of the function  h(x)=x^3 in the range [0, 10],
    on the one set of axes."

Program imports two libraries: numpy and matplotlib.pyplot, then generates a list of 1000 random numbers from a normal distribution with a mean of 5 and a standard deviation of 2 using the numpy library and stores it in "numbers" variable(*Reference 1.*).<br>
Next, the program defines values for x in **h(x)=x^3** and creates a list of these values in the range from 0 to 10 using a for loop and stores them in "xcubed" variable.<br>
Afterward, the program defines and assigns various styles for plot elements. (*Reference 2. and 3.*)<br> Then creates the various labels and assigns styles to them. The title font style is set separately so it can be displayed with a different font style. Exponent in "h(x)=x^3" formula set to superscript in all occurences. (*Reference 4. and 5.*)<br>
The program then plots the histogram of the 1000 random numbers from the normal distribution using the hist() function from matplotlib, with the colour of the bars being set to green as shown in the lecture, colours defined by hexacode. Program also plots the function h(x)=x^3 using the plot() function from matplotlib, with custom colour and line style.<br>
A legend is configured to the plot with labels for the histogram and function h(x)=x^3. The plot is then displayed using the show() function.

#### - *References:* 
##### *1. numpy ref: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html*
##### *2. matplotlib ref: https://matplotlib.org/stable/tutorials/introductory/quick_start.html*
##### *3. customise default style ref: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot*
##### *4. change font style for title ref: https://stackoverflow.com/questions/29426075/how-to-modify-the-font-size-in-matplotlib-venn/70231723#70231723*
##### *5  superscript ref: https://stackoverflow.com/questions/21226868/superscript-in-python-plots*