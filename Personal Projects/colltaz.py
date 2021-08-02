from typing import Counter


num = float(input("Please enter your starting number:\n"))
counter = 0
# if number isn't 1, enter loop

while num != 1:
    # Check if num is even
    counter += 1
    if (num % 2 == 0):
        num = num / 2
        print("Current number after", counter, "steps is:", num)
    else:
        num = num * 3 + 1
        print("Current number after", counter, "steps is:", num)
else:
    print("Reached 1 in", counter, "steps")
