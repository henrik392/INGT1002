binary = "100.0111"

result = 0

for (i, c) in enumerate(binary.split(".")[1]):
    result += int(c) * 2**(-i-1)

for (i, c) in enumerate(binary.split(".")[0][::-1]):
    result += int(c) * 2**(i)

print(result)