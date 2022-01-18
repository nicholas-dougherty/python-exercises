# 1.)
'''
I've rented some movies for my kids: 
The little mermaid (for 3 days), Brother Bear (5 days),
and Hercules (1 day). If price for a movie per day is
3 dollars, how much will I have to pay?
'''

['Little Mermaid', 'Brother Bear', 'Hercules']
total_days_per_title = 3 + 5 + 1
daily_rental_fee = 3
total_cost = daily_rental_fee * total_days_per_title
# daily_rental_fee * (days_per_title)
print(total_cost, 'dollars is nothing. Anything for my imaginary kids.')
# $27 

# 2.)
'''
Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
and Facebook 350. How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
'''
amazon_payout = 380 * 4
facebook_payout = 350 * 10
google_payout = 400 * 6
paycheck = google_payout + facebook_payout + amazon_payout 
print('This week I am banking', paycheck, 'dollars!')
# psh, I wish. 

# 3.) 
'''
A student can be enrolled to a class only if the class is not full and the class 
schedule does not conflict with her current schedule.
'''
def elibility():
    pass
eligible = 'Class added to schedule.'
ineligible = 'Error. See enrollment manual.'
# set Boolean values for these statements to false. 
seats_unavailable = 0
classes_conflict = 0
# if either case is present, FALSE, or failure to enroll. 
if seats_unavailable or classes_conflict:
    eligibility()
    print(ineligible)
else:
    print(eligible)


# 4.)
'''
A product offer can be applied only if people buys more than 2 items, and the offer
 has not expired. Premium members do not need to buy a specific amount of products.
'''
def offer():
    pass
success = 'Thanks for shopping with us.'
failure = 'Go on. GET. not git. GET!'
# the only real stipulations here. 
cart_minimum = 3
premier_deal = 1
# Me as a shopper.
cart_count = 69
premier_membership = 0

if(cart_count >= cart_minimum 
    or premier_deal != 0):
    offer()
    print(success)
else:
    print(failure)

# experiencing a syntax error when attempting to move or to the subsequent line
# made the mistake of using a colon instead of equal sign when creating variables
#                                                                            No clue why.
#

# 5.) 
''' Use the following code to
follow the instructions below.
    username = 'codeup'
    password = 'notastrongpassword'
Create a variable that holds a boolean values for each of the following conditions: 
a.) the password must be at least 5 characters
b.) the username must be no more than 20 characters
c.) the password must not be the same as the username
(B-B-B-BONUS) neither the username or password can start or end with whitespace.
'''

def registration():
    pass

username = 'codeup'
password = 'notastrongpassword' #meta

password_minimum = 5
username_maximum = 20

grant_username = len(username) <= username_maximum
grant_password = len(password) >= password_minimum
grant_complete = username != password 
# grant_stripper_king = 

registered = 'Account creation complete.'
rejected = 'Did not meet account criteria. Try again.'

if(grant_username and grant_password and grant_complete):
    registration()
    print(registered)
else:
    print(rejected)

# I will return and test for a whitespace strip later. 