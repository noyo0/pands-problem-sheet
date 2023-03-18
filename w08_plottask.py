# plottask.py
# Author: Norbert Antal
# Weekly Task 8
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x**3 in the range [0, 10], on the one set of axes.
# Program generates a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2. 
# Additionally, it plots the function h(x)=x^3 in the range of [0,10] on the same graph.
# numpy ref: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# matplotlib ref: https://matplotlib.org/stable/tutorials/introductory/quick_start.html
# customise default style ref: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
# superscript ref: https://stackoverflow.com/questions/21226868/superscript-in-python-plots


import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.normal(5,2,1000) # 1000 values with a mean of 5 and standard deviation of 2
# ------ h(x)=x**3--------------->
xcubed=[]
for i in range(0,11):
    x=i**3
    xcubed.append(x)
#---------------------------------I
#-----------def plot styles------------------------------>
ax=plt.axes()
ax.set_facecolor("#F0F4EF")
plt.grid(True, color="#799377")
small = 8
med = 10
big = 14
plt.rc("font", size=small)          # controls default text sizes
plt.rc("axes", titlesize=small)     # fontsize of the axes title
plt.rc("axes", labelsize=med)    # fontsize of the x and y labels
plt.rc("xtick", labelsize=small)    # fontsize of the tick labels
plt.rc("ytick", labelsize=small)    # fontsize of the tick labels
plt.rc("legend", fontsize=small)    # legend fontsize
plt.rc("font", family="serif")          # controls default text style
specfont1 = {"family":"serif","color":"#4a6741","size":14}
#--------------------------------------------------------------I
#---------------labels---------------------->
plt.title("""Week 08 task - A histogram of a normal distribution 
of 1000 values with a mean of 5, and standard deviation of 2, 
and a plot of the function  h(x)=$\mathregular{x^3}$ in the range [0, 10]""", fontdict=specfont1)
plt.xlabel("Normal distribution",color="#4a6741")
plt.ylabel("h(x)=$\mathregular{x^3}$", color="#E74C3C")
#-------------------------------------------I
#--------plotting ----------->
plt.hist(numbers,color="#4a6741")
plt.plot(xcubed,color="#E74C3C",linestyle="dotted")
#-----------------------------I
plt.legend(["h(x)=$\mathregular{x^3}$","Normal distribution"])
plt.show()