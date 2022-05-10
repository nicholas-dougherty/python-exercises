# Import Exercises
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Terminology
# 
# Before going into imports, let's discuss some terminology:
# 
# A Module is an python file with a .py extension.
# 
# Modules contain functions and variables. A module can exist in:
# 
#      The python standard library
#      Community developed packages
#      Your working directory as a file that you have created.
#
# A Package is a directory that contains modules.
# 
# It can also consist of other packages, or 'sub-packages'. Packages are a way to distribute one or more modules. We install     #        packages in order to be able to import modules or libraries for use.
# 
# A Library is a collection of code, data, documentation, and configuration, usually purpose built for specific tasks.
# 
# Libraries can be very large in scope like numpy, a library the forms the base for most other scientific packages in python, or # matplotlib, the library we'll use for data visualization. Other libraries are smaller in scope, like requests, a library for   #  sending HTTP requests.
# 
# The Python Package Index, PyPI, https://pypi.org/, is a repository of community developed Python packages.
# 
# Anaconda's Conda product is a package manager. It helps you find and install 3rd party packages.
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
import function_exercises as fun
fun.is_vowel('a')

from function_exercises import calculate_tip

fun.calculate_tip(50.25, .2)
dir(fun)


from inspect import getmembers, isfunction
print(getmembers(calculate_tip, isfunction))
help(calculate_tip)

# help is one way to check a functions parameters. jupyterlab enables it through shift-tab in parentheses 
# alternatively, type the function and a question mark after in jupyter lab and execute the cell.
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# 2. Read about and use the itertools module from the python standard library 
#    to help you solve the following problems:

# a. How many different ways can you combine the letters from "abc" 
#    with the numbers 1, 2, and 3?

import itertools
aseasyas = ('a', 'b', 'c', 1, 2, 3)
len(list(itertools.combinations(aseasyas, 2))) # 15
len(list(itertools.combinations(aseasyas, 3))) #20

# b. How many different combinations are there of 2 letters from "abcd"?

import itertools
from itertools import combinations
a2d = ('a', 'b', 'c', 'd')
list(itertools.combinations(a2d, 2)) 
len(list(itertools.combinations(a2d, 2))) # 6

# c. How many different permutations are there of 2 letters from "abcd"?

import itertools
from itertools import combinations
a2d = ('a', 'b', 'c', 'd')
list(itertools.permutations(a2d, 2)) 
len(list(itertools.permutations(a2d, 2))) # 12

# 3. Save this file as profiles.json inside of your exercises directory.
# Use the load function from the json module to open this file.

import json
json.load(open('profiles.json'))

# Your code should produce a list of dictionaries. Using this data, 
# write some code that calculates and outputs the following information:

# a. Total number of users
import json
dict = json.load(open('profiles.json'))
len(dict) # 19

# b. Number of active users
import json
dict = json.load(open('profiles.json'))
activeuser = 0
for user in dict: 
    if user['isActive']:
        activeuser += 1

print(activeuser) #9

# c. Number of inactive users
import json
dict = json.load(open('profiles.json'))
inactiveuser = 0
for user in dict: 
    if user['isActive'] == 0:
        inactiveuser += 1

print(inactiveuser) #10

# d. Grand total of balances for all users
import json
dict = json.load(open('profiles.json'))
total = 0
for user in dict:


# e. Average balance per user
import json
dict = json.load(open('profiles.json'))

# f. User with the lowest balance
import json
dict = json.load(open('profiles.json'))

# g. User with the highest balance
import json
dict = json.load(open('profiles.json'))

# h. Most common favorite fruit
import json
dict = json.load(open('profiles.json'))

# i. Least most common favorite fruit
import json
dict = json.load(open('profiles.json'))

# j. Total number of unread messages for all users
import json
dict = json.load(open('profiles.json'))

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------