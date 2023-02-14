P = [1, 5, 89, 100, -254, 300, -5031, -2, 0, 425, 892, 69, 6969, -69, -6969, 13, 21, 37, -21, -37]
# S_P = sorted(P)
# print(S_P)
searching_num = 69


def searcher(set_of_content, searching):

    sorted_set_of_content = sorted(set_of_content)
    beginning = 0
    end = len(sorted_set_of_content) - 1
    middle = (beginning + end) // 2

    if searching == middle:
        print(f"Searching number {searching} is in given set!!!")

    elif searching < middle:
        end = middle -1

    else:
        beginning = middle + 1



    # print(sorted_set_of_content, searching)


searcher(P, searching_num)
