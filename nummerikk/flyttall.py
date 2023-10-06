import numpy as np

bits = "11.001001000"

x = np.pi

print("x = ", x)

guess = 0
i = 0
for bit in bits:
    if bit == ".":
        guess *= 2**(i)
        i = 0
        continue

    guess += int(bit) * 2**(-i-1)
    i += 1

print("x = ", x)
print("guess = ", guess)
print("x - guess = ", x - guess)
