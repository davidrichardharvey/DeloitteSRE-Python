# Lists (Arrays)

# sre = ["Sacha", "Viktor", "Amy"]
# print(sre)
# print(type(sre))
#
# print(sre.append("Zeeshan"))
# print(sre)
# sre.append("Michael")
# print(sre)
# sre.append("Akunma")
# print(sre)
# sre.append("Viktor")
# print(sre)
# sre.remove("Viktor")
# print(sre)
#
# last_thing = sre.pop(3)
# print(sre)
#
#
# print(f"{last_thing} was removed")
#
# print(sre.index("Amy"))
# print(sre.count("Amy"))
# print(len(sre))
#
# print(sre.sort(reverse=True))
# print(sre)
# sre.append("Zeeshan")
# print(sre)
# print(sre.index("Zeeshan"))
# print(sre.index("Zeeshan",1))


# Tuple

essentials = ("bread", "milk", "chocolate", "cheese")
print(essentials)
print(type(essentials))
print(essentials[0])
print(essentials.count("bread"))

print(essentials.index("chocolate"))

# IMMUTABLE = Cannot be changed
# MUTABLE = Can be changed

mixed = (45, 4.6, None, "Hello")
print(mixed)