import typing

a = 5
print(type(a))
a = "pięć"
print(type(a))
a = [5, "pięć"]
print(type(a))


def przeliteruj(word: str) ->  List[str]:
    return list(word)

print(przeliteruj("Python"))
