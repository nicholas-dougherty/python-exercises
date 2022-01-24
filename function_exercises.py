# 1.) Define a function named is_two. It should accept one input and return True
#  if the passed input is either the number or the string 2, False otherwise.

def is_two(two):
    return two == 2 or two == "two" or two == '2'

# is_two("two") # True
# is_two(2) # True
# is_two('2') # True
# is_two(4) # False
# is_two("six") # False
# print(is_two(222222))

def is_two(n):
    n == 2 or n == '2'
# assert is_two(2) == True # assertions aren't working for me. 

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

# is_vowel('vowel') #false
# is_vowel('e') #true
# is_vowel('T') #false
# is_vowel('U') #true

def is_vowel(somestring):
    if type(somestring) == str:
        result = somestring.lower() in ['a', 'e', 'i', 'o', 'u']
        return result
    else:
        return False
 
# 3.) Define a function named is_consonant. It should return True if the passed
#  string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(l):
    l = l.lower()
    if is_vowel(l) == False:
        return True
    else:
        return False
    
# is_consonant('e')
# is_consonant('g')
# is_consonant('a')
# is_consonant('j')

def is_consonant():
    if type(somestring) == str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel(somestring)
    return False

# 4.) Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def cap_cons(str):
    str = str.lower()
    if is_consonant(str[0]):
        return str.capitalize()
    else:
        return str

# cap_cons('dolphin') #capitalized first word. Awesome. 
# cap_cons('eagle') #didn't capitalize first word. Bingo. 

def caps_con(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if caps_con(first_letter):
        string = string.capitalize()
    return string

# 5.) Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percentage, bill):
    return percentage * bill

# calculate_tip(.15, 90) # $13.5

def total(float):
    return calculate_tip(.15, 90) + float

# total(90): # $103.5 I'd like to do this in a less specifically self-contained way. 
# I will make this more complex in a bit. Just trying to get through the exercises.

def calculate_tip(bill, tip_percentage=0.2):
    if type(bill) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage must be between 0 and 1'
    return tip_percentage * bill

# 6.) Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.

def apply_discount(original, discount):
    return original - (original * discount)

# apply_discount(10, .2) # $8.00. Success. 

def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount

# 7.) Define a function named handle_commas. It should accept a string that is a number
#  that contains commas in it as input, and return a number as output.

def handle_commas(str):
    return str.replace(',', '')


def handle_commas(somestring):
    if type(somestring) != str:
        return 'input must be string'
    somestring = somestring.replace(',', '')
    if somestring.isdigit():
        return float(somestring)
    else:
        return 'input must be a string that is a number'

#   look into the try function: (try: except:)
# handle_commas('2,000,000') # 2000000 Check. 

# 8.) Define a function named get_letter_grade. It should accept a number and return 
#  the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'
    else: 
        return 'Input must be a number'

# get_letter_grade(89) # B. Right.
# get_letter_grade(69) # D. Correct.
# get_letter_grade(73) # C. YUP.

# 9.) Define a function named remove_vowels that accepts a string and returns a 
#  string with all the vowels removed.

def remove_vowels(str):
    str = str.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in str if letter.lower() not in vowels]
    result = ''.join(result)
    return result
print(remove_vowels)

# remove_vowels('dingus') #dngs. Sweet. 

def remove_vowels(str):
    str = str.lower()
    vowels = 'aeiouAEIOU'
    result = [letter for letter in str if letter.lower() not in vowels]
    result = ''.join(result)
    return result
print(remove_vowels)

# remove_vowels('dingus') #dngs again. 

def remove_vowels(somestring):
    if type(somestring) != str:
        return False
    output = ''
    for letter in somestring:
        if is_consonant(l):
            output += l
    return output


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

def normalize_name(string):
    output = '' 
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
        output = output.strip
        output = output.replace(' ', '_')
        return output


# normalize_name('DolPhins Are sO CoOl')

# 11.) Write a function named cumulative_sum that accepts a list of numbers and 
#    returns a list that is the cumulative sum of the numbers in the list.
#    cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#    cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list):
    total = 0
    for x in list:
        total += x
        yield total

# list(cumulative_sum([1, 2, 3, 4]))

somenums = [1,2,3,4,5]
for placeholder, num in enumerate(somenums):
    print('index: ', placeholder)
    print(num)

def cumulative_sum(somenums):
    output = []
    for i, num in enumerate(somenums):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output