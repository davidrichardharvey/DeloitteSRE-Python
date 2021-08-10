# IF

# age = 15
#
# if age == 15:
#     print("You are just old enough")
# elif age > 15:
#     print("You can watch this slightly violent film.")
#     print("This is still in the if statement block")
# else:
#     print("You are too young")
#     print("Still part of the else-block")
#
# print("This will always run")

film_rating = "U"

age = input("What is the film rating? U, PG, 12A, 15, 18?:\n")

if age.upper() == "U": #Something that will be resolved true or false followed by :
    print("Everyone can watch this!")
elif age.upper() == "PG":
    print("If you're under 15, You need a Parent!")
elif age.upper() in ("12A", "12"):
    print("If youre 12 youre fine!")
elif age == "15":
    print(" You have to be 15 to watch this movie!")
elif age == "18":
    print("Being 18+, Go enjoy all the films")
else:
    print("Please specify the correct film rating of U, PG, 12A, 15, 18!")



# match age:
#     case "U":
#         do something
#     case "PG":
#         do something else
#     case "12" | "12A":
#         do a thing
#     case _:



# Get user input for their age and the film cert
# Print an appropriate message
# Think about how to handle casting inputs
# Try to make the code robust (idiot proof)