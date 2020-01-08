def print_table(n: int) -> None:

    numbers = list(range(1, n+1))

    for i in numbers:
        print('\t' + str(i), end='')

    print()

    for i in numbers:

        print(i, end='')
        for j in numbers:
            print('\t' + str(i * j), end='')

        print()
