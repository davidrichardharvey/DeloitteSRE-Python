# def print_something(word1, word2):
#     print("print")
#     print(word1)
#     print(word2)
#     print("")
#
#
# print("This is outside the function definition")
#
# print_something("dog", "woof")
# print_something("cat", "miaow")
# print_something("rabbit", "squeak")
# # print_something("mouse", "squeak")
# returned_numbers = []
#
#
# def add_plus_one(int1: int, int2: int) -> int:
#     a = int1 + int2 + 1
#     return a
#
#
# x = add_plus_one(3, 6)

def average(*multiargs):
    total = sum(multiargs)
    count = len(multiargs)
    return total / count


print(average(1, 4, 6))
print(average(456, 35462, 4574, 234, 45674, 2345, 3563))

# Build a calculator by defining functions for the following:
# addition
# subtraction
# multiplication
# division