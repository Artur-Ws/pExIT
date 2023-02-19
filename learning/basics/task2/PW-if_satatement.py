name = str(input("Hi there. What's your name? "))

if name == "":
    print("Give me at least one letter")

elif not name.isalpha():
    print("You've added at least one digit to your name (by accident I hope)")

else:
    print(f"Nice to meet you {name}")

    maths_op = str(input("Wanna multiply two numbers or add them? If multiply type M, If addition type A: "))

    if maths_op == str("M"):
        num_1 = float(input("Ok then. Give me first number: "))
        num_2 = float(input("The second number is: "))

        result = num_1 * num_2

        print(f"The result of multiplying {num_1} and {num_2} is {result}")
    elif maths_op == str("A"):
        num_1 = float(input("Ok then. Give me first number: "))
        num_2 = float(input("Ok then. Give me first number: "))

        result = num_1 + num_2
        print(f"The result of addition {num_1} and {num_2} is {result}")
    else:
        print("It in not an option. Good night.")
