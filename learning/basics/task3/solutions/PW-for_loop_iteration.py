"""
Given list contains all prime numbers in range 1-100. Write code to ask user to type number in range 1-100,
then check if this number is in the prime_numbers list, if it is, print that the number typed by user is prime,
if it's not - print that it is complex number. Also check if number provided by user is in allowed range,
if not ask as long as user will provide correct number

Tip: use `while` loop to check if provided number is correct, and `for` loop to iterate over prime_numbers list
not necessary to create function, but you can if you want to.
"""

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

user_number = input("Type a number in range 1-100 ")

while not user_number.isdigit() or int(user_number) not in range(1, 101):
    user_number = input("Give me a number in range 1-100: ")

is_number_found = False

for i in prime_numbers:
    if i == int(user_number):
        print(f"The number {user_number} is a prime number.")
        is_number_found = True
        break

if not is_number_found:
    print(f"The number {user_number} is a complex number.")
