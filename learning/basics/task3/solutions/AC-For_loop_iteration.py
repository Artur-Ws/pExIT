
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

while True:
    try:
        user_type = int(input("Type a number in range 1-100 -> "))
    except ValueError:
        print("NUMBER please!")
    else:
        if user_type in range(1, 100):
            break
        else:
            print("This number is not within range, please enter a valid number.!")

for i in prime_numbers:
    if user_type in prime_numbers:
        print(f"{user_type} is prime!")
        break
    else:
        print(f"{user_type} is complex!")
        break
