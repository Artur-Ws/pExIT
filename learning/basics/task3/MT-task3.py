# """
# Given list contains all prime numbers in range 1-100. Write code to ask user to type number in range 1-100,
# then check if this number is in the prime_numbers list, if it is, print that the number typed by user is prime,
# if it's not - print that it is complex number. Also check if number provided by user is in allowed range,
# if not ask as long as user will provide correct number
# Tip: use `while` loop to check if provided number is correct, and `for` loop to iterate over prime_numbers list
# not necessary to create function, but you can if you want to.
# """
#
# prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def validate_input(num):
    if not num.isdigit():
        return False

    num = int(num)

    if num < 1 or num > 100:
        return False

    return True


num = input("Please enter a number in the range 1-100: ")

while not validate_input(num):
    num = input("Invalid input. Please enter a number in the range 1-100: ")

num = int(num)

if num in prime_numbers:
    print(f"The number {num} is prime.")
else:
    print(f"The number {num} is complex.")
