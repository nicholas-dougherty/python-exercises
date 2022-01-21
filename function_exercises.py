# 1.) Define a function named is_two. It should accept one input and return True
#  if the passed input is either the number or the string 2, False otherwise.

def is_two(two):
    return two == 2 or two == "two"

is_two("two") # True
is_two(2) # True
is_two('2') # False
is_two(4) # False
is_two("six") # False


# 2.) Define a function named is_vowel. It should return True if the passed
#  string is a vowel, False otherwise.

#def is_vowel(vowel):
 #   vowel = vowel.lower()
#    return(vowel == 'a' or vowel == 'e'
 #   or vowel == 'i' or vowel == 'o' 
 #   or vowel == 'u')
 #this works but I don't like the way it looks 
#is_vowel('I') # True
#is_vowel('i') # True
#is_vowel('F') # False
#is_vowel('O') # True
#is_vowel('B') # False

def is_vowel(l):
    l = l.lower()
    if l in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

is_vowel('f') #false
is_vowel('e') #true
is_vowel('T') #false
is_vowel('U') #true

# all good. Working perfectly. Needs to be more succinct though. 
 
# 3.) Define a function named is_consonant. It should return True if the passed
#  string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(l):
    l = l.lower()
    if is_vowel(l) == False:
        return True
    else:
        return False
    
is_consonant('e')
is_consonant('g')
is_consonant('a')
is_consonant('j')




# 4.) Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def cap_cons(str):
    str = str.lower()
    if is_consonant(str[0]):
        return str.capitalize()
    else:
        return str

cap_cons('dolphin') #capitalized first word. Awesome. 
cap_cons('eagle') #didn't capitalize first word. Bingo. 

# 5.) Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percentage, bill):
    return percentage * bill

calculate_tip(.15, 90) # $13.5

def total(float):
    return calculate_tip(.15, 90) + float

total(90): # $103.5 I'd like to do this in a less specifically self-contained way. 
# I will make this more complex in a bit. Just trying to get through the exercises.

# 6.) Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.

def apply_discount(original, discount):
    return original - (original * discount)

apply_discount(10, .2) # $8.00. Success. 

# 7.) Define a function named handle_commas. It should accept a string that is a number
#  that contains commas in it as input, and return a number as output.

def handle_commas(str):
    return str.replace(',', '')

handle_commas('2,000,000') # 2000000 Check. 

# 8.) Define a function named get_letter_grade. It should accept a number and return 
#  the letter grade associated with that number (A-F).

def get_letter_grade(int):
    if int >= 90:
        return 'A'
    elif int >= 80:
        return 'B'
    elif int >= 70:
        return 'C'
    elif int >= 60:
        return 'D'
    else:
        return 'F'

get_letter_grade(89) # B. Right.
get_letter_grade(69) # D. Correct.
get_letter_grade(73) # C. YUP.

# 9.) Define a function named remove_vowels that accepts a string and returns a 
#  string with all the vowels removed.

def remove_vowels(str):
    str = str.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in str if letter.lower() not in vowels]
    result = ''.join(result)
    return result
print(remove_vowels)

remove_vowels('dingus') #dngs. Sweet. 

def remove_vowels(str):
    str = str.lower()
    vowels = 'aeiouAEIOU'
    result = [letter for letter in str if letter.lower() not in vowels]
    result = ''.join(result)
    return result
print(remove_vowels)

remove_vowels('dingus') #dngs again. 

# 10.) Define a function named normalize_name. It should accept a string and 
#   return a valid python identifier, that is:
#   anything that is not a valid python identifier should be removed
#   leading and trailing whitespace should be removed
#   everything should be lowercase
#   spaces should be replaced with underscores
#   for example: Name will become name First Name will become first_name
#   % Completed will become completed

def normalize_name(str):
    str = str.strip()
    str = str.lower()
    str = str.replace(' ', '_')
    return str

normalize_name('DolPhins Are sO CoOl')

# 11.) Write a function named cumulative_sum that accepts a list of numbers and 
#    returns a list that is the cumulative sum of the numbers in the list.
#    cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#    cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list):
    total = 0
    for x in list:
        total += x
        yield total

list(cumulative_sum([1, 2, 3, 4]))
