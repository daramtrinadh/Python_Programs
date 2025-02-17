# re.findall()
import re

numbers=re.findall(r'\d+','The year 2025 have 12 months with 28 days ')
print(numbers)
nondigit=re.findall(r'\S','This year is 2025 with 12 months')
print(nondigit)