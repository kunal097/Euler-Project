fib_sum = 0

a = 1
b = 1

while fib_sum <= 4000000:
    c,a = a+b,b
    b = c

    if c%2 == 0:
        fib_sum+=c


print(fib_sum)
