# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Location(latitude={self.latitude}, longitude={self.longitude})"
#
#     def __str__(self):
#         return f"({self.latitude}, {self.longitude})"
#
# bham_academy = Location(latitude=52.488647, longitude=-1.887249)
# print(bham_academy)
#
# print(repr(bham_academy))

#
# n = 0.003453
# print(f"Fixed Point: {n:f}")
# print(f"Exponential Notation: {n:e}")

class Cat:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old cat"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old cat"
        elif format_spec == "cat":
            return f"A {self.age * 5} cat-years old cat"
        else:
            return self.__str__()

whiskers = Cat(6)

print(f"Whiskers is {whiskers}")
print(f"Whiskers is {whiskers:dog}")
print(f"Whiskers is {whiskers:cat}")