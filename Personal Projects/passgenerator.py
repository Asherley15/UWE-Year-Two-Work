import random
import string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
symb = string.punctuation
length = 12
list = upper + lower + symb
temp = random.sample(list, length)
passw = "".join(temp)
print(passw)
