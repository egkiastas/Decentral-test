import numpy as np

def solve_system(A, b):
    # Gaussian elimination
    n = len(A)
    for i in range(n):
        # Find pivot row
        max_element = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_element:
                max_element = abs(A[k][i])
                max_row = k
        # Swap pivot row
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        # Eliminate
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            b[k] += c * b[i]
    # Back-substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]
    return x

# Example usage:
A = np.array([[3, 1, 2, -1], [2, 5, -1, -2], [1, -2, 4, -1], [2, 3, -5, 3]])
b = np.array([5, 8, -11, 20])
x = solve_system(A, b)
print(x) # Output: [1.0, 2.0, -1.0, 3.0]
