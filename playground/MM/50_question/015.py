a = "python_moj_kod.py"
b = "python_notatki.txt"


def is_python_py(name):

    return True if name[0:6] == 'python' and name[-3:] == ".py" else False


print(is_python_py(a))
print(is_python_py(b))


z = "In the face of ambiguity, refuse the temptation to guess."

print(z[-6:])