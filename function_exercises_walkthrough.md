# Function Exercises Walkthrough

## Exercise 1.)

> Define a function named is_two. It should accept one input and return True
> if the passed input is either the number or the string 2, False otherwise.

```
# This is_two function defines a single parameter, two, which could be either
# a string or integer, and is thus programmed to return a boolean value on 
# the basis of whether the input registers as the number two or strings of 2. 
def is_two(two):
    # evaluation underway. Anything not set to equal the parameter will
    # be rejected through returning as false. 
    return two == 2 or two == "two" or two == '2'
```

Walkthrough:

1. When passing the integer 2, the conditional evaluates True, this boolean
is then returned and revealed through the print() function. Subsequently,
True is printed in our interactive console. The same goes for '2' and 'two.'

```
print(is_two(2))
print(is_two('2'))
print(is_two("two"))
```

```
>>> True
>>> True
>>> True 
```

1. Any arguments not set to coincide with the value of the function as set 
via the parameter will be expressed as False. 

```
print(is_two('too'))
print(is_two('to'))
print(is_two(222222))
```
```python
>>> False
>>> False
>>> False
```

## Exercise 2.)

> Define a function named is_vowel. It should return True if the passed
> string is a vowel, False otherwise.

```
# This is_vowel) function is again based on Boolean foundations. It accepts
# its singular parameter, l (an imagined alias of 'letter'), and returns 
# True if the input or argument is a vowel, as determined through inclusion
# in a list. 
def is_vowel(l):
    # the lower() function guarantees that capitalized input would match
    # the list requirements. Alternatively, the list, or a string like 
    # 'aAeEiIoOuU' would accomplish the same end goal. 
    l = l.lower()
    # this is the list that acts as the basis for checking the boolean validity.
    if l in ('a', 'e', 'i', 'o', 'u'):
    # if within the aforementioned list, return True
        return True
    # if there isn't a match, return false.
    else:
        return False
```

Walkthrough:

1. Due to the inclusion of the .lower() function, the argument is not case sensitive.
So, any vowel, except for the occasional 'y' in words like 'gym', will evaluate as True. 
As before, the boolean value will be displayed thanks to the print() function. 

```
print(is_vowel('e'))
```
```
>>> True
```
```
print(is_vowel('I'))
```
```
>>> True
```
2. Any alternative, whether it be a letter not explicitly lain out in the or a string
possessing more than a single-letter, will return false after the function's invocation.

```
print(is_vowel('vowel'))
```
```
>>> False
```
```
print(is_vowel('F'))
```
```
>>> False
```

## Exercise 3.)

> Define a function named is_consonant. It should return True if the passed
> string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

```
# this functions first two lines are functionally identical to is_vowel.
def is_consonant(l):
    l = l.lower()
    # Herein lies the change, this time it is assigned to detect whether 
    # the is_vowel function returns False
    if is_vowel(l) == False:
    # if so, then it must be a consonant, assuming the input is bound to 
    # the previously stated assumptions. 
        return True
    # otherwise, it is in fact a vowel, and cannot be returned as a consonant.
    else:
        return False
```

Walkthrough:

1. In order for an argument to pass as a consonant, it must first cycle through
the is_vowel function, which has been implemented as an element within is_consonant().
So, if anything other than a vowel is keyed, it evaluates through is_vowel as false
and is afterward returned as True. Print() yields the result. 

```
print(is_consonant('F'))
```
```
>>> True
```

2. Otherwise, when a vowel is passed, falsity is the outcome. is_vowel processes
any of those five letters as true, which in turn is processed as false, as per
the requirements addressed in the IF clause. 

```
print(is_consonant('U'))
```
```
>>> False
```

## Exercise 4.)

> Define a function that accepts a string that is a word. The function should 
> capitalize the first letter of the word if the word starts with a consonant.

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 5.)

> Define a function named calculate_tip. It should accept a tip percentage 
> (a number between 0 and 1) and the bill total, and return the amount to tip.

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 6.)

> Define a function named apply_discount. It should accept a original price, and a 
> discount percentage, and return the price after the discount is applied.

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 7.)

> Define a function named handle_commas. It should accept a string that is a number
> that contains commas in it as input, and return a number as output.

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 8.)

> Define a function named get_letter_grade. It should accept a number and return 
> the letter grade associated with that number (A-F).

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 9.)

> Define a function named remove_vowels that accepts a string and returns a 
> string with all the vowels removed.

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 10.)

> Define a function named normalize_name. It should accept a string and 
> return a valid python identifier,

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```

## Exercise 11.)

> Write a function named cumulative_sum that accepts a list of numbers and 
> returns a list that is the cumulative sum of the numbers in the list.

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```python
[result of demo code here]
```