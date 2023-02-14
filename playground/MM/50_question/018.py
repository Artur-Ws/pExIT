def is_divided_1(a, b):

    return max(a, b) % min(a, b) == 0


def is_divided_2(a, b):

    if a % b == 0:
        return True
    elif b % a == 0:
        return True
    else:
        return False


print(is_divided_1(5, 115))
print(is_divided_2(3, 297))

a = 123454321

b = 11111


print(a % b == 0)
