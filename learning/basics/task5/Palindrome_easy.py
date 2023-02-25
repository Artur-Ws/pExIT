"""
Palindrome is expression which looks the same whether you read it from the beginning or the end. Example of palindromic
numbers: 121, 5445, 53835, 123454321

Implement a function that will check if given number is palindrome. Function should return boolean value (True or False)
"""
palindromes = [12321, 543345, 9048409, 25452]
not_palindromes = [123421, 1232, 987689]


def is_palindrome(number):
    # put your code here (and remove "pass" keyword)
    pass


# test section - do not change code below!
# It will check if your implementation is correct and will inform you if it is not, just look at error log.
for number in palindromes:
    assert is_palindrome(number), f"Number {number} is palindrome! Your function says it is not!"
for number in not_palindromes:
    assert not is_palindrome(number), f"Number {number} is not palindrome! Your function says it is!"
