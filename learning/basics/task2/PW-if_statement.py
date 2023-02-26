name = input("Hi there. What's your name? ")

while name == "" or not name.isalpha():
    if name == "":

        name = input("Give me at least one letter ")

    elif not name.isalpha():
        name = input("You've added at least one digit to your name (by accident I hope). Try again ")

print(f"Nice to meet you {name}")

maths_op = input("Wanna multiply two numbers or add them? For multiplication type M, for addition type A: ")

while not (maths_op == str("A") or maths_op == str("M")):
    maths_op = input("For multiplication type M, for addition type A ")

if maths_op == "M":
    num_1 = float(input("Ok then. Give me the first number: "))

    num_2 = float(input("The second number is: "))

    result = num_1 * num_2

    print(f"The result of multiplying {num_1} and {num_2} is {result}")

elif maths_op == "A":

    num_1 = float(input("Ok then. Give me the first number: "))

    num_2 = float(input("Ok then. Give me the second number: "))

    result = num_1 + num_2

    print(f"The result of addition {num_1} and {num_2} is {result}")
