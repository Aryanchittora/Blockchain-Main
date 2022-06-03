import re


no = int(input('Enter a number : '))
power = int(input('Enter a power : '))

# result = pow(no, power)
result = eval('no ** power')
print(f'{no} raised to {power} is = {result}')

if result > 0:
    print(f'{result} is Positive')
else:
    print(f'{result} is Negative')