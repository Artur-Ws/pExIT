def greeting(name):
    print(f"Hello {name}, nice to meet you")

names = ["Patrycja", "Mieszko", "Paweł"]

#two ways to print greeting, using names from list

print(names)

for name in names:
    
    greeting(name)

i = 0

while i < 3:

    greeting(names[i])

    i += 1