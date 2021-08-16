import os

parent_dir = os.path.dirname(__file__)
filepath = os.path.join(parent_dir + "/lunch_order.txt")
# #
# try:
#     with open(filepath, 'r') as file:
#         data = list(map(lambda x: x.strip('\n'), file.readlines()))
#         print(data)
# except FileNotFoundError as errmsg:
#     print("Could not find the right file", errmsg)
# finally:
#     print("This will happen if there is or isn't an error")

# r = Open for reading
# w = Open for writing *
# x = eXclusive creation - creates a new file (fails if already exists)
# a = Appending (instead of overwriting)
# t = Text mode (combined with above)
# b = Binary mode
# + = Updating (reading AND writing)

def write_order_to_file(filepath, order_item):
    try:
        with open(filepath, "x") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("Get the file path right, you fool!")
        raise

write_order_to_file("new_file.txt", "Eggs on Toast")
write_order_to_file(filepath, "Quiche")

# Read from a drinks order file (e.g. drinks_order.txt)
# Check that each drink in the order is available
# in the drinks_menu.txt
# What should happen if it isn't?