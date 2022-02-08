height = int(input("Please enter the width of the base"))
size = height
for i in range(height):
    print("\n")
    for i in range(size):
        print('*', end=" ")
    size -= 1
    # if size == 1:
