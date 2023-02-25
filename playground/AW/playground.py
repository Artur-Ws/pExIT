def calculate():
    numbers = []
    for i in range(5000, 5556):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return numbers


print(calculate())