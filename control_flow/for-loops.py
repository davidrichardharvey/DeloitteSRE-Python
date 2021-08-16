# Iterator

# Iterate over X

numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 3:
#         print("MY FAVOURITE!")
#     else:
#         print(f"The number is {num}")
# print("The for loop has ended")

# nested_list = [[1, 2, 3], [4, 5], [6]]
# for sub_list in nested_list:
#     print(sub_list)
#     for num in sub_list:
#         print(num)
#
# book = {
#     "name": "The Iliad",
#     "author": "Homer",
#     "rating": 7
# }
#
# for key, value in book.items():
#     print(f"The {key} is {value}")

library = [
    {
        "title": "The Iliad",
        "author": "Homer",
        "rating": 7
    },
    {
        "title": "The Foundations of Mathematics",
        "author": "Ian Stewart & David Tall",
        "rating": 8.5,
        "synopsis": "LOTS OF MATHS"
    },
    {
        "title": "The Very Hungry Caterpillar",
        "author": "Eric Carle",
        "rating": 10,
        "synopsis": "Caterpillar eats lots and transforms."
    }
]

# Iterate through library
# If the book has a synopsis, print the title and synopsis

# for book in library:
#     if "synopsis" in book:
#         print(f"{book['title']}: {book['synopsis']}")

# for book in library:
#     synopsis = book.get("synopsis")
#     if synopsis:
#         print(f"{book['title']}: {synopsis}")


for i in range(5,10):
    print(i)