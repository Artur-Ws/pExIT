# '''
# Create new file "<initials>-<task_name>" in this directory, there you should solve this task.
# This file should stay unchanged! Example: "AW-input_print.py"
# You should know if-statement before this task. Example:
# if variable == 5:
#     print("It is 5!")
# else:
#     print("It is not 5!")
# Use code your from task1, extend it to check if name provided by user is valid (not empty, string-type),
# if not, print message that name is not valid. then ask if user wants to multiply, or add numbers,
# use if statement to perform correct operation.
# '''

# test - do not read
# name = input("Hello, what is sprudo joke? \n")
# if name == "beniz":
#     print("Haha beniz!")
# else:
#     print("You are so boring!")


name = input("Hello, what is your name? \n")

if name.isalpha():
    print(f"Hello {name} put first number to multiply")
else:
    print("Invalid name!")
    print("Hi anonymous hacker put first number to multiply...")

number1 = int(input(""))
print("Put second number to multiply")
number2 = int(input(""))
print(f"{number1 * number2}")
