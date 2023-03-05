
palindromes = [12321, 543345, 9048409, 25452]
not_palindromes = [123421, 1232, 987689]


def is_palindrome(number):
    str_number = str(number)
    reversed_str_number = str_number[::-1]
    return str_number == reversed_str_number


print(is_palindrome(543345))

for number in palindromes:
    assert is_palindrome(number), f"Number {number} is palindrome! Your function says it is not!"
for number in not_palindromes:
    assert not is_palindrome(number), f"Number {number} is not palindrome! Your function says it is!"
