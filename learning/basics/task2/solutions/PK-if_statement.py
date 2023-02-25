name = input("Hello! What is your name? ")

if name == "":

    print("Don't be rude. Introduce yourself!")

elif name.isalpha() == False:

    print("Don't be rude. Introduce yourself with real name!")

else:

    choice = input('Would you like to multiply or add numbers? Type multiply or add. ')

    if choice.capitalize() == "Multiply":

        number_1 = int(input("Type first number to multiplication "))

        number_2 = int(input("Type second number to multiplication "))

        print(f"{name.capitalize()}, your result of multiplication for {number_1}, and {number_2} is  {number_1 * number_2}")

    elif choice.capitalize() == "Add":

        number_1 = int(input("Type first number to addition. "))

        number_2 = int(input("Type second number to addition. "))

        print(f"{name.capitalize()}, your result of addition for {number_1}, and {number_2} is  {number_1 + number_2}")

    else:
        
        print("Type correct command please.")
