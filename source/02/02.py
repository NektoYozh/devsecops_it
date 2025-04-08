import random
import math

a = random.randint(-10,10)
b = random.randint(-10,10)

c = a * b

print(a, b)

if c == 0:
    print("Одно из чисел равняется нулю.")
elif c < 0:
    print(a+b)
else:
    if a > 0:
        print(math.fabs(a-b))
    else:
        print(c)
