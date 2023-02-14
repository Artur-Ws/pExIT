import os


def catalogue_content(cat_pat):

    for el in os.listdir(cat_pat):

        el_path = os.path.join(cat_pat, el)

        if os.path.isdir(el_path):
            catalogue_content(el_path)

        else:
            print(el_path)


pt = input("Whats this? ")
catalogue_content(pt)
