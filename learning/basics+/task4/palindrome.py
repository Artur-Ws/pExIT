"""
Before this task I suggest to complete task5 from basics.

Palindrome is expression which looks the same whether you read it from the beginning or the end. Example of palindromic
numbers: 121, 5445, 53835, 123454321

Implement a function that will return all palindromic numbers in given range as a list of numbers.
function should get 2 arguments: start and end of range (both - start and end number should be included!)
function should return list of integers
"""


def get_palindromes(start, end):
    # put your code here (and remove "pass" keyword)
    pass


# test section - do not change code below!
# It will check if your implementation is correct and will inform you if it is not, just look at error log.
expected_100_200 = [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
expected_5005_5555 = [5005, 5115, 5225, 5335, 5445, 5555]
assert expected_100_200 == get_palindromes(100, 200), f"Expected palindromes in range (100, 200) is: " \
                                                      f"{expected_100_200}\nyour function says it is: " \
                                                      f"{get_palindromes(100, 200)}"

assert expected_5005_5555 == get_palindromes(5005, 5555), f"Expected palindromes in range (5005, 5555) is: " \
                                                          f"{expected_5005_5555}\nyour function says it is: " \
                                                          f"{get_palindromes(5005, 5555)}"
