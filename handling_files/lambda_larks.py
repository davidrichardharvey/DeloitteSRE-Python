# Lambda Functions

def add(n1, n2):
    return n1 + n2
print(add(2, 4))

add = lambda n1, n2: n1 + n2
print(add(2, 4))

# Map
def double_add_one(n):
    return (n * 2) + 1

nums = [1, 2, 3, 4, 5]
new_nums = list(map(double_add_one, nums))
print(new_nums)
new_nums = list(map(lambda n: (n * 2) + 1, nums))
print(new_nums)

savings = [234.00, 555.00, 674.00, 78.00]
savings = list(map(lambda n: n * 1.10, savings))
print(savings)
# implement this using map and a lambda function

# Filter
def is_even(n):
    return n % 2 == 0

greater_than_200 = lambda y: y > 200

print(list(filter(is_even, nums)))
# Write the above using a lambda function
even_nums = filter(lambda x: x % 2 == 0 and x > 200, range(210))


# AND NOW FOR SOMETHING COMPLETELY DIFFERENT

# List Comprehension

savings = [234.00, 555.00, 674.00, 78.00]
bonus = [x + x/10 for x in savings]
print(bonus)

large_savings = [x for x in savings if x > 500]
print(large_savings)

large_savings_bonus = (x + x/10 for x in savings if x > 500)
print(large_savings_bonus)