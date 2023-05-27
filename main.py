import file1
import file2


# for exercise 6.2.5
def main():
    greeting_card = file1.GreetingCard()
    birthday_card = file2.BirthdayCard()

    greeting_card.greeting_msg()
    print("-------------")
    birthday_card.greeting_msg()


if __name__ == "__main__":
    main()

