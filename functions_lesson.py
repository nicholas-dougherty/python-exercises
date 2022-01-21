#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~                            Python Functions                            ~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Topics Covered:
# - Using Functions
# - Defining Functions
# - Function Scope
# - Lambda Function Expressions

############################### Using Functions ###############################

# Function Vocabulary
#
# - run (execute inside of a statement)/ invoke / call
# - argument (values passed to a function)
# - return value (the value a function produces)

# We've already used some built-in functions

type('abc')
print('Hey there!')

# TODO: take a look at the code snippet below:
max([1, 2, 3])

# What is the function name? MAX
# Where is the function invocation? Gets the maximum number
# What is the return value? 3

# TODO: What will the output of the following code be? Why? Explain step-by-step
type(max([1, 2, 3])) 
#   Type identifies the class. Integer. It seeks the maximum amoung these integers.

# TODO: What will the output of the following code be? Why?
type(max)
# shows that max is a function. 

# What other built-in functions do you know?
# upper, lower, pow
############################## Defining Functions ##############################

# Function Vocabulary
#Function is a reusable piece of code that takes an input and gives output
# - Function Definition- INCREMENT: takes a number and returns the number plus one. 
# - Function Name
# - Parameter
# - Function Body- indented  lines, guts of the function.

def increment(n):
    return n + 1

# TODO: What is the difference between the increment function above and the one below?
def increment(n):
    print(n + 1)

# increment(increment(3)) returns 5.
# substition model of evaluation
# a function invocation is replaced with its return value. 

# TODO: define a function named is_weekend. This function should accept a string and return true if the string is either saturday or sunday, false otherwise.
is_weekend = ['M', 'T', 'W', 'R', 'F', 'SA', 'SU']
if is_weekend.startswith('S'):
    True
else:
    False

def is_weekend(some_day):
    some_day = some_day.lower()
    return some_day == 'saturday' or some_day == 'sunday'

# TODO: test out your is_weekend function with various values.

is_weekend('friday')
is_weekend('tuesday')
is_weekend('saturday')

# TODO: Use your is_weekend function in combination with input() and an if statement to prompt the user for a day of the week and tell them whether or not it is a weekend.

user_input = input('Please enter a weekday: ')
if is_weekend(user_input):
    print('It\s a weekend')
else:
    print('It\s a weekday.')
# TODO: Create a function named nonzero. It should accept a number and return true if the number is anythong other than zero, false otherwise.

nonzero = input('Type a number: ')
if input != 0:
    print('Nice')
else:
    print('Pahaha')

def nonzero(x):
    return x != 0
nonzero(123)


# TODO: Use your nonzero function in combination with the built-in input function and an if statement to prompt the user for a number and print a message displaying whether or not the number is zero.

user_input = int(input('please enter a number: '))
if nonzero(user_input):
    print('It is not zero!')
else: 
    print('That\s a zero')

# TODO: Transfer the work you have done into a function named explain_nonzero. Calling this function should prompt the user and display the message as before.

def explain_nonzero():
    user_input = int(input('please enter a number: '))
    if nonzero(user_input):
        print('It is not zero!')
    else: 
        print('That\s a zero')

## Default Parameter Values and Keyword Arguments ##

# - Positional Argument
# - Keyword Argument

def add(x, y):
    return x + y

def sayhello(name="Innis"):
    return f"Hello, {name}!"

# TODO: call the say hello function and don't pass any arguments
sayhello()
# TODO: call the say hello function and pass your name as a string argument both positionally and as a keyword argument.
sayhello("Nick")
sayhello(name="Nick")
## Docstrings ##
def sayhello(name="Innis"):
    "Provides a friendly greeting."
    return f"Hello, {name}!"

# Aside: built-in help with help() (or ? in ipython)

################################ Function Scope ################################
#
# - scope refers to defining variables inside/outside of functions
# - scope defines where a variable can be referenced
# - global and local scope

# TODO: look at the example below. What do expect will happen when you run it?
def f():
    x = 123
f()
print(x)

# TODO: look at the example below. What do expect will happen when you run it?
x = 123
def f():
    print(x)
f()

# TODO: look at the example below. What do expect will happen when you run it?
x = 123
def f(x):
    return x + 1
print(f(12))

# TODO: What is the difference between local and global scope? Which is preferred?

# TODO: Take a look at the code below. Before running it, think about what you would expect to happen. Explain step by step how the python code is executing.
def changeit(x):
    x = x + 1

x = 42
print(x)
changeit(x)
print(x)

## Function Scope Example ##
def fill_nulls(df):
    return df.fillna(0)

def drop_outliers(df):
    outlier_cutoff = 3
    return df[df.zscore().abs() < outlier_cutoff]

def prep_dataframe(df):
    df = fill_nulls(df)
    df = drop_outliers(df)
    return

# Data Prep example: https://github.com/CodeupClassroom/darden-nlp-exercises/blob/main/nlp_prepare.py
# The specifics here aren't important right now, just pay attention to the overall shape of functions and how local scope is used.

############################### Lambda Functions ###############################
#
# - A function as an expression
# - used for "throw away", or one-off, functions

def increment(n):
    return n + 1
# same as
increment = lambda n: n + 1

# lambda structure
# lambda --> (followed by) the thing --> : --> what the thing should do. 

# Use case: sorting (min, max)
#
# Python doesn't know how to compare dictionaries, but it does know how to compare strings or numbers

students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]

# sort by name
sorted(students, key=lambda s: s["name"])

# TODO: write the code necessary to sort by grade
sorted(students, key=lambda s: s["grade"])

# TODO: Write the code necessary to sort the list of student dictionaries by student <em>last</em> name.
sorted(students, key=lambda s: s["name"].split()[-1])
# Hint: You will need to write a function that takes in a student dictionary and returns just the last name.
# Hint: You can use the <code>.split</code> string method to seperate the first name and the last name.
