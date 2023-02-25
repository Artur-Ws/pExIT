import math

def field_square(a):
    return a * a

def field_rectangle(a, b):
    return a * b

def field_circle(r):
    return math.pi * r ** 2

def field_triangle(a, b):
    return 0.5 * a * h

def field_trapeze(a, b, h):
    return (a + b) / 2 * h

from enum import IntEnum

Menu_Figures = IntEnum("Menu_Figures", "Rectangle Square Triangle Trapeze Circle Close")

while True:
    print("Field of which figure you want to count")
    print('1 - Rectangle')
    print("2 - Square")
    print("3 - Triangle")
    print('4 - Trapeze')
    print("5 - Circle")
    print("6 - Close")

    choice = int(input("Type index: "))
    if choice == Menu_Figures.Rectangle:
        a = float(input("Type first side of rectangle: "))
        b = float(input("Type first side of rectangle: "))
        field = field_rectangle(a, b)
        print(field)

    elif choice == Menu_Figures.Square:
        a = float(input("Type side of square: "))
        field = field_square(a)
        print(field)

    elif choice == Menu_Figures.Triangle:
        a = float(input("Type first side of triangle: "))
        b = float(input("Type second side of triangle: "))
        field = field_triangle(a, b)
        print(field)

    elif choice == Menu_Figures.Trapeze:
        a = float(input("Type first side of trapeze: "))
        b = float(input("Type second side of trapeze: "))
        h = float(input("Type height of trapeze: "))
        field = field_trapeze(a, b, h)
        print(field)
    
    elif choice == Menu_Figures.Circle:
        r = float(input("Type radius: "))
        field = field_circle(r)
   
    elif choice == Menu_Figures.Close:
        break
    else:
        print("Uncorrect value")