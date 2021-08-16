prompt_user = True

while prompt_user:
    age = input("What is your age?\n")
    if age.isdigit():
        if int(age) < 120:
            age = int(age)
            prompt_user = False
        else:
            print("Don't be silly")
    else:
        print("Please provide age in digits")

# Add this while logic to your film certificate code
# Ensure you get a valid age and a valid film certificate