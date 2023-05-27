import file1


# for exercise 6.2.5
class BirthdayCard(file1.GreetingCard):
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch', sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print("Happy birthday")
        print(self._sender_age)
