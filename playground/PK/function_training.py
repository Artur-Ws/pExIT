# write a code that will sum all numbers in range 1 to number typed by a user
import time

i = int(input("Type number that will be last number of sum "))

# first way - for loop
def sum_1(i):
    sum_value = 0
    for number in range(1,i+1):
        sum_value = sum_value + number

    return sum_value

# second way - generator list
def sum_2(i):
    return sum([number for number in range(1,i+1)])

# third way - generator set
def sum_3(i):
    return sum({number for number in range(1,i+1)})

#fourth way - generator
def sum_4(i):
    return sum((number for number in range(1,i+1)))

#third way - math
def sum_5(i):
    return (1 + i) / 2 * i
    
#time performance counter
def finish_timer(start):
    end = time.perf_counter()
    return end - start

def x(funcion,arg):
    start = time.perf_counter()
    print(funcion(arg))
    print(finish_timer(start))


# function inside function
# def function_performance(func):
#     func()

# def show_message():
#     print("message")

# function_performance(show_message)

x(sum_1, i)

# start = time.perf_counter()
# print(sum_1(i))
# finish_timer(start)


# print(sum_2(i))
# print(sum_3(i))
# print(sum_4(i))
# print(sum_5(i))
