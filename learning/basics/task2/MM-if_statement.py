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


class IfStatementApp:

    def __init__(self):
        self.name = input("Hello! What is your name? ")
        self.name = self.__name_checker__()
        self.numbers = []

    def main_process(self):

        action = input(f"{self.name}, do You want to do some crazy multiplying shit or regular adding? (for multiplying type 'm', for adding type 'a'): ")

        if action == "m":
            self.calculator("multiply", "multiplication")
        elif action == "a":
            self.calculator("add", "adding")
        else:
            os.system(exit("Application exit code: Wrong answer"))

    def get_number(self, op_verb):

        self.numbers.append(self.__num_checker__(input(f"{self.name}, give me first number to {op_verb}: ")))
        self.numbers.append(self.__num_checker__(input(f"Now give me second number {self.name}: ")))

        return self.numbers

    def calculator(self, op_verb, op_noun):
        self.numbers = self.get_number(op_verb)

        if op_verb == "multiply":
            calculation = self.numbers[0] * self.numbers[1]
        elif op_verb == "add":
            calculation = self.numbers[0] + self.numbers[1]

        print(f"{self.name}, Your result of {op_noun} for {self.numbers[0]} and {self.numbers[1]} is {round(float(calculation),4)}!!!")

    def __name_checker__(self):

        if self.name == "":
            print("All right Nameless Noob, keep Your secrets...")
            self.name = "Nameless Noob"
        elif self.name.isalpha():
            self.name = self.name.capitalize()
        else:
            os.system(exit("Application exit code: No real name detected!"))

        return self.name

    def __num_checker__(self, num):

        try:
            num = int(num)
        except ValueError:

            try:
                num = float(num)
            except ValueError:
                os.system(exit("Application exit code: Entered character is not a number value!"))
        return num


if __name__ == "__main__":

    IfStatementApp().main_process()
