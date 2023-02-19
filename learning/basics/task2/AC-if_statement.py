
def typing_username():
    while True:
        username = input("Hello! What is your name? ")
        if username == "":
            print("Come on, name like that doesn't exist. Try again (At least 1 figure)")
        else:
            print (f"Hello {username}.")
            break


def adding():
    number_1 = None
    number_2 = None
    while number_1 is None:
        number_1_str = input("First -> ")
        try:
            number_1 = int(number_1_str)
        except:
            print("Sorry, numbers only :)")

    while number_2 is None:
        number_2_str = input("Second -> ")
        try:
            number_2 = int(number_2_str)
        except:
            print("Sorry, numbers only :)")

    print(f"Sum of your numbers is  {number_1 + number_2}")


def multiplying():
    number_1 = None
    number_2 = None
    while number_1 is None:
        number_1_str = input("First -> ")
        try:
            number_1 = int(number_1_str)
        except:
            print("Sorry, numbers only :)")

    while number_2 is None:
        number_2_str = input("Second -> ")
        try:
            number_2 = int(number_2_str)
        except:
            print("Sorry, numbers only :)")

    print(f"Multiplication of your numbers is  {number_1 * number_2}")


def choosing_what_to_do():
    choosing = input("""Would u like to add or multiply 2 numbers? "A" for adding or "M" for multiplying. -> """)
    if choosing == ("A".casefold()):
        adding()
    elif choosing == ("M".casefold()):
        multiplying()
    else:
        choosing_what_to_do()


typing_username()
choosing_what_to_do()
