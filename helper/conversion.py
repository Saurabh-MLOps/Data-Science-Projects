
import re

number = r"\d+(,\d{3})*\.*\d*"


'''
TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

money_conversion("$12.2 million") --> 12200000
money_conversion("$790,000") --> 790000

use test_money_conversion.py to test your solution
'''
def money_conversion(money):
        value_string = re.search(number, money).group()
        value = float(value_string.replace(",",""))
        return value
        
        # strip out the commas before solution
        
	

print(re.search(number, "12.2").group())
print(re.search(number, "790,000.25").group())
