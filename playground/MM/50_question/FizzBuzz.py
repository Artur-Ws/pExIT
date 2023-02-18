def fizzbuzz(last_number):

    for num in range(1, int(last_number) + 1):

        if num % 15 == 0:
            print("FizzBuzz")

        elif num % 5 == 0:
            print("Buzz")

        elif num % 3 == 0:
            print("Fizz")

        else:
            print(num)


number = input("Whats the border number? ")
fizzbuzz(number)
