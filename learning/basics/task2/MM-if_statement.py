import os

'''
Create new file "<initials>-<task_name>" in this directory, there you should solve this task.
This file should stay unchanged! Example: "AW-input_print.py"

You should know if-statement before this task. Example:
if variable == 5:
    print("It is 5!")
else:
    print("It is not 5!")

Use code your from task1, extend it to check if name provided by user is valid (not empty, string-type),
if not, print message that name is not valid. then ask if user wants to multiply, or add numbers,
use if statement to perform correct operation.

'''


class InputPrinter:

    def __init__(self):
        self.name = input("Hello! What is your name? ")

    def main_process(self):

        name = self.__name_checker__()
        multiplying = input(f"{name}, do You want to do some crazy multiplying shit or regular adding? (for multiplying type 'm', for adding type 'a'): ")

        if multiplying == "m":
            self.multiplier()
        elif multiplying == "a":
            self.adder()
        else:
            os.system(exit("Application exit code: Wrong answer"))

    def multiplier(self):

        name = self.__name_checker__()

        first_number = input(f"{name}, give me first number to multiply: ")
        self.__int_checker__(first_number)

        second_number = input(f"Now give me second number {name}: ")
        self.__int_checker__(second_number)

        print(f"{name}, Your result of multiplication for {first_number} and {second_number} is {int(first_number) * int(second_number)}!!!")

    def adder(self):

        name = self.__name_checker__()
        first_number = input(f"{name}, give me first number to add: ")
        self.__int_checker__(first_number)

        second_number = input(f"Now give me second number {name}: ")
        self.__int_checker__(second_number)

        print(f"{name}, Your result of adding for {first_number} and {second_number} is {int(first_number) + int(second_number)}!!!")

    def __name_checker__(self):

        if self.name == "":
            print("All right Nameless Noob, keep Your secrets...")
            self.name = "Nameless Noob"

        else:
            pass

        return self.name

    def __int_checker__(self, num):

        try:
            int(num)
        except ValueError:
            os.system(exit("Application exit code: Entered character is not a number value!"))

        return num


if __name__ == "__main__":

    InputPrinter().main_process()
