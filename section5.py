class IDIterator:
    def __init__(self, id=1):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while not check_id_valid(self._id) and self._id < 999999999:
            self._id += 1

        if self._id == 999999999:
            raise StopIteration()
        return self._id


def id_generator(id_number):
    while True:
        while not check_id_valid(id_number) and id_number < 999999999:
            id_number += 1
        if id_number == 999999999:
            return
        yield id_number
        id_number += 1


def check_id_valid(id_number):
    id_number_list = [int(digit) for digit in str(id_number)]
    total = 0

    for i in range(len(id_number_list)):
        if i % 2 != 0:
            id_number_list[i] = id_number_list[i] * 2
            if id_number_list[i] > 9:
                id_number_list[i] = id_number_list[i] % 10 + id_number_list[i] // 10
        total += id_number_list[i]

    if total % 10 == 0:
        return True
    return False


def main():
    id_number = int(input("Enter a 9-digit ID: "))
    preference = input("Generator or Iterator? (gen/it)? ")

    if preference == 'gen':
        id_iterator = id_generator(id_number + 1)
    else:
        id_iterator = IDIterator(id_number + 1)

    count = 0
    for id in id_iterator:
        if count == 10:
            break
        print(id)
        count += 1


if __name__ == "__main__":
    main()
