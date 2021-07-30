x = int(input("Please enter the vaalue of X"))
y = int(input("Please enter the vaalue of Y"))
z = x
x = y
y = z
check = input("Which value would you like printed?")
if check == 'x':
    print(x)
if check == 'y':
    print(y)
