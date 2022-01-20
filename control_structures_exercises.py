# 1.)Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not
print('What day of the week is it?')
day = input()

if day in('Monday', 'M', 'Mon'):
    print('It is Monday.')
else:
    print('Thankfully it is not Monday.')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

print('What day of the week is it? Use the following format: M, T, W, R, F, S, Su')
day = input()

if day in('M', 'T', 'W', 'R', 'F'):
    print('Today is a weekday. WEAK.')
else:
    print('The weekend is upon us.')


# c. create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck.
#You get paid time and a half if you work more than 40 hours'''

weekly_hours = 50
hourly_rate = 27
overtime = hourly_rate * 1.5
if weekly_hours <= 40:
    payout = weekly_hours * hourly_rate
else: 
    payout = (40 * hourly_rate) + ((weekly_hours - 40) * overtime)
print(payout)
# 2.) Loop Basics

# a.) While
#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.'''

int = 5
while int <= 15:
    print(int)
    int += 1

#for number in range(5, 16):
    #print(number)
    #this gives the same output. 

    #? why is it that if print is put on the following line, it goes from 6 to 16?
    
# i. Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

int = 0
while int <= 100:
    print(int)
    int += 2


# ii. Alter your loop to count backwards by 5's from 100 to -10.

count = 100

while count >= -10:
    print(count)
    count = count - 5
# alternatively

int = 100
while int >= -10:
    print(int)
    int -= 5


# iii. Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000. Output should equal:
int = 2
while int < 1000000:
    print(int)
    int = int * int
    # this runs and calculates in notebook, but not here. 

# iv. Write a loop that uses print to create the output shown below (descending by five)

count = 100
while count >= 5:
    print(count)
    count -= 5

# 2b.) FOR LOOPS

# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

number = input('Enter an integer.')
for x in range(1, 11):
    print(number, 'x', x, '=', int(number) * x)

# ii. Create a for loop that uses print to create the output shown below

number = 1
for x in range(1, 10):
    print(str(x) * number)
    number += 1

    #what a strange riddle.

# 2c.) Break and Continue. 
# Prompt the user for an odd number between 1 and 50. 
#Use a loop and a break statement to continue prompting the user if they enter 
#invalid input. (Hint: use the isdigit method on strings to determine this).
# Use a loop and the continue statement to output all the odd numbers between 
# 1 and 50, except for the number the user entered

#odd_choice = input('Enter an odd number between 1-50.')
#for x in range(1, 51):
    #print(x)
    #if x == odd_choice
    #print('Yikes! Skipping number:', ' ', x)

# no, I'm on the wrong track here. Return later. 

# 2d. 
#The input function can be used to prompt for input and use that input
 #in your python code. Prompt the user to enter a positive number and write
#  a loop that counts from 0 to that number. (Hints: first make sure that
 #  the value the user entered is a valid number, also note that the input 
#   function returns a string, so you'll need to convert this to a numeric type.)
while True:
    user = input('Enter a positive integer.')
    if user.isdigit():
        break
user = int(user)
for x in range(user +1):
    print(x)

#2e. Write a program that prompts the user for a positive integer. Next write a loop
#    that prints out the numbers from the number the user entered down to 1.

# 3.) Fizzbuzz

# One of the most common interview questions for entry-level programmers
# is the FizzBuzz test. Developed by Imran Ghory, the test is designed 
# to test basic looping and conditional logic skills.

#  Write a program that prints the numbers from 1 to 100.
#   For multiples of three print "Fizz" instead of the number
#    For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".'''

# 4.) Display a table of powers.

# Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.'''

# 5.) 
#Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges: A : 100 - 88 B : 87 - 80 C : 79 - 67 D : 66 - 60 F : 59 - 0


# 6.) 
# Create a list of dictionaries where each dictionary represents a book that
# you have read. Each dictionary in the list should have the keys title, author, and genre.
# Loop through the list and print out information about each book.

#Prompt the user to enter a genre, then loop through your books list and print
# out the titles of all the books in that genre.
