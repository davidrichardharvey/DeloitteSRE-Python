def add(int1, int2):
    return int1 + int2


def subtract(int1, int2):
    return int1 - int2


def multiply(int1, int2):
    return int1 * int2


def divide(int1, int2):
    return int1 / int2


def calculator(instruction, int1, int2):
    if instruction == "add":
        return add(int1, int2)
    if instruction == "subtract":
        return subtract(int1, int2)
    if instruction == "multiply":
        return multiply(int1, int2)
    if instruction == "divide":
        return divide(int1, int2)


# print(calculator("add", 2345, 345))