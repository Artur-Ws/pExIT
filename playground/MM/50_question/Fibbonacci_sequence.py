# A = [0 1 2 3 4 5 6  7  8  9 10]
# B = [0 1 1 2 3 5 8 13 21 34 55]

def fibonacci_sequence (item):

    fib_seq = []
    fib_seq_beginning = [0, 1]

    if item == 0:
        fib_seq.append = 0

    elif item == 1:
        fib_seq.append = 0, 1

    else:
        fib_seq = fib_seq_beginning

        for i in range(2, int(item) + 1):

            fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq[int(item)]


number = input("What's the sequence expression? ")
print(fibonacci_sequence(number))











