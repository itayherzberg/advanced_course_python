
def question1():
    with open('names.txt', 'r') as f:
        print(max(f.read().splitlines(), key=len))


def question2():
    with open('names.txt', 'r') as f:
        print(sum(list(map(lambda x: len(x), f.read().splitlines()))))


def question3():
    with open('names.txt', 'r') as f:
        file_as_lst = f.read().splitlines()
        shortest_name = min(list(map(lambda x: len(x), file_as_lst)))
        print('\n'.join([name for name in file_as_lst if len(name) == shortest_name]))


def question4():
    with open('names.txt', 'r') as f1, open('name_length.txt', 'w') as f2:
        for length in list(map(lambda x: len(x), f1.read().splitlines())):
            f2.write(str(length) + '\n')


def question5():
    with open('names.txt', 'r') as f:
        number = int(input("Enter a number: "))
        print('\n'.join([x for x in f.read().splitlines() if len(x) == number]))


def main():
    question5()


if __name__ == "__main__":
    main()
