import os


def wypisz_zawartosc_katalogu(path):

    for element in os.listdir(path):
        path_element = os.path.join(path, element)

        if os.path.isdir(path_element):
            wypisz_zawartosc_katalogu(path_element)

        else:
            print(path_element)


wypisz_zawartosc_katalogu(r"D:\Użytkownicy\Maliccy\Dokumenty\Mateusz\PROGRAMOWANIE\Python\Projekty\50_questions\testowy")
