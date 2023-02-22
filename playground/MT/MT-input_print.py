# '''
# Create new file "<initials>-<task_name>" in this directory, there you should solve this task.
# This file should stay unchanged! Example: "AW-input_print.py"
# Create a script that will ask about name, and two numbers tu multiply.
# Script should display greetings and result of multiplication.
# Example:
#     out: Hello! What is your name?
#     > Artur
#     out: Hello Artur, give me first number to multiply!
#     >5
#     out: now give me second number.
#     >3
#     out: Artur, your result of multiplication for 3 and 5 is 15!
# IMPORTANT: Learn about f-strings in python, use them to print messages!
# '''
print("Hello, what is your name?")
name = input("")
print("Hi {name} put first number to multiply".format(name=name))
number1 = int(input(""))
print("Put second number to multiply".format(number1=number1))
number2 = int(input(""))
print(f"{number1 * number2}")


