x = input("Hello! What is your name? ")
print(f"Hello {x}!, give me two numbers and i will multiply them.")
y = None
z = None
while y == None:
    y_str = input("First -> ")
    try:
        y = int(y_str)
    except:print("Sorry, numbers only :)")

while z == None:
    z_str = input("Second -> ")
    try:
        z = int(z_str)
    except:print("Sorry, numbers only :)")


print(f"Multiplication of your numbers is  {y * z}")