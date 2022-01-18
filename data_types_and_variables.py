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

