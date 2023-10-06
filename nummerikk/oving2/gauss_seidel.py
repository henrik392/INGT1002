import numpy as np
r1, r2, r3 = np.array([1, 5, 1, 7]), np.array(
    [12, 7, 3, 22]), np.array([2, 7, -11, -2])
A = np.concatenate((r2, r1, r3)).reshape(3, 4)
b = np.array(A[:, 3])
A = np.array(A[:, 0:3])
x = np.array([0, 0, 0])
iterasjoner = 1
n = np.shape(A)[0]
for k in range(0, iterasjoner):
    for i in range(0, n):
        x[i] = b[i]
        for j in range(0, n):
            if i != j:
                x[i] = x[i] - A[i, j]*x[j]
        x[i] = x[i]/A[i, i]
    print(x)

print("\n\n", np.linalg.solve(A, b))
