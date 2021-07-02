n = int(input("What number of the Fib Seq are you looking for?"))
i = 0
fib1 = 1
fib2 = fib1
k = 0
while i < n:
    i = i + 1
    fib3 = fib1 + fib2
    print(fib1)
    fib1 = fib2
    fib2 = fib3
