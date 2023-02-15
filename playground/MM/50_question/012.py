def is_palindrom_1(word):

    word_list = []

    for letter in word:
        word_list.append(letter)

    return True if "".join(word_list) == "".join(list(reversed("".join(word_list)))) else False


print(is_palindrom_1('kajak'))
print(is_palindrom_1('anakonda'))

a = 'kajak'
b = list(reversed(a))
print(b)


def is_palindrom_2(word):

    reversed_word = word[::-1]

    if word.lower() == reversed_word.lower():
        print(True)

    else:
        print(False)


is_palindrom_2('kajak')
is_palindrom_2('anakonda')
is_palindrom_2('Anna')

def is_palindrom_3(word):

    return True if word == word[::-1] else False


print(is_palindrom_3('kajak'))
print(is_palindrom_3('anakonda'))
print(is_palindrom_3('Anna'))
