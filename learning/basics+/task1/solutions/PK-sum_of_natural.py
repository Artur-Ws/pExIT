"""
All natural numbers (zero is considered a natural number for the purposes of the problem)
divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14, 15]. The sum of these numbers is: 51.
Find the sum of all numbers divisible by 5 or 7 less than 100.
Present the solution in the form of a function called calculate().
In response, call the calculate() function and print the result to the console.
Expected result:
1580
"""


def calculate():
    sum_of_numbers = sum([number for number in range(1,101) if number % 7 == 0 or number % 5 == 0 and number < 100])
    return sum_of_numbers

result = calculate()
print(result)
