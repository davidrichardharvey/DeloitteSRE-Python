# # String Slicing
# #        012345678910
# # hello = "Hello World!"
# # print(hello[-1]) # lo Wo
#
# # String Methods
#
# whitespace = "      Here is a string with space             "
# print(whitespace)
# print(whitespace.strip())
# print(whitespace.find("s"))
#
# print(whitespace.count(" "))
# print(whitespace.strip().count(" "))
#
# # lower and upper methods
# print(whitespace.lower())
# print(whitespace.upper())
#
# print(whitespace.replace("e","ooo"))
# # text = "here is. a really quick. example."
# # print(text.capitalize())
#
# a = "45634"
# b = "453b"
# c = "3.14"
# print(a.isdigit())
# print(b.isdigit())
# print(c.isdigit())
# print(c.isnumeric())


name = "Lassie"
years = 7
height = 60.2
# print(name + " is " + str(years) + " years old and " + str(height) + "cm tall.")
# print(f"{name} is {years} years old and {height}cm tall.")

# pi = 3.14159265359
# print(f"Pi: {pi}")
# print(f"Pi to 3dps: {pi:.3f}")
# print(f"Pi to 5dps: {pi:.5f}")
# print(f"Pi to 0dps: {pi:.0f}")
#
# score = 16
# max_score = 26
#
# print(f"You scored {score/max_score}")
# print(f"You scored {score/max_score:.2f}")
# print(f"You scored {score/max_score:%}")
# print(f"You scored {score/max_score:.2%}")
# print(f"You scored {score/max_score:.0%}")
# print(f"You scored {score/max_score:e}")
#
# big_num = 235.676


# Booleans

t = True
f = False
# print(t, f)
#
# print("Hello" == "Hello")
# print("Blue" != "Yellow")
# print(10 > 100)
# print(10 < 100)
# print(1 <= 1)
# print(1 >= 1)

weather = "Miserable"
sky = "Grey"
# print(weather == "Good" or sky == "Blue")

# hello = "helloworld"
# print(hello.isalpha())
# print(hello.islower())
# print(hello.isupper())
# print(hello.endswith("d"))
# print(hello.startswith("hell"))
#
# x = 0
# y = 1
# print(bool(x))
# print(bool(y))
# print(bool(-1))
# print(bool(3 + 2j))
#
# print(int(True), int(False))
#
# print(1 + True)
# print(1 and True)

# None

a = None
print(a)
print(type(a))

print(bool(None))

print(None is False)

print(a == None)
print(a is None)

b = 1 < 2
print(b)