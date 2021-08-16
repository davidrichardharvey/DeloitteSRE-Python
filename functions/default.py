def repeat_greeting(message="Hello!", number_of_times=3, upper=False):
    if upper:
        print(message.upper() * number_of_times)
    else:
        print(message * number_of_times)


repeat_greeting()
repeat_greeting("hey", 7, True)
repeat_greeting("howdy")
repeat_greeting(upper=True)


class Dog:
    def __init__(self, name: str,
                 legs: int = 4):
        self.name = name
        self.legs = legs


fido = Dog("Fido")
stool = Dog("Stool", 3)

lassie = Dog(
    name="Lassie",
    legs=4
)

