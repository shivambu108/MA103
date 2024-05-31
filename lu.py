# import numpy as np

# def lu_decomposition(A):
#     n = len(A)
#     L = np.eye(n)
#     U = A.copy()

#     for k in range(n-1):
#         for i in range(k+1, n):
#             factor = U[i, k] / U[k, k]
#             L[i, k] = factor
#             U[i, k+1:] -= factor * U[k, k+1:]

#     return L, U

# def forward_substitution(L, b):
#     n = len(b)
#     y = np.zeros(n)

#     for i in range(n):
#         y[i] = b[i] - np.dot(L[i, :i], y[:i])

#     return y

# def backward_substitution(U, y):
#     n = len(y)
#     x = np.zeros(n)

#     for i in range(n-1, -1, -1):
#         x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

#     return x

# # User input for matrix A
# rows_A = int(input("Enter the number of rows for matrix A: "))
# cols_A = int(input("Enter the number of columns for matrix A: "))
# A = np.zeros((rows_A, cols_A))

# for i in range(rows_A):
#     for j in range(cols_A):
#         A[i, j] = float(input(f"Enter the element A[{i+1},{j+1}]: "))

# # User input for vector b
# b = np.zeros(cols_A)
# for j in range(cols_A):
#     b[j] = float(input(f"Enter the element b[{j+1}]: "))

# # LU decomposition
# L, U = lu_decomposition(A)

# # Solve Ly = b
# y = forward_substitution(L, b)

# # Solve Ux = y
# x = backward_substitution(U, y)

# print("\nMatrix A:")
# print(A)

# print("\nMatrix L:")
# print(L)

# print("\nMatrix U:")
# print(U)

# print("\nSolution for y in Ly = b:")
# print(y)

# print("\nSolution for x in Ux = y:")
# print(x)


import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = A.copy()

    for k in range(n-1):
        for i in range(k+1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            # Adjusted to subtract multiples of the entire row, including elements below the diagonal
            U[i, k:] -= factor * U[k, k:]

    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x

# User input for matrix A
rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
A = np.zeros((rows_A, cols_A))

for i in range(rows_A):
    for j in range(cols_A):
        A[i, j] = float(input(f"Enter the element A[{i+1},{j+1}]: "))

# User input for vector b
b = np.zeros(cols_A)
for j in range(cols_A):
    b[j] = float(input(f"Enter the element b[{j+1}]: "))

# LU decomposition
L, U = lu_decomposition(A)

# Solve Ly = b
y = forward_substitution(L, b)

# Solve Ux = y
x = backward_substitution(U, y)

print("\nMatrix A:")
print(A)

print("\nMatrix L:")
print(L)

print("\nMatrix U:")
print(U)

print("\nSolution for y in Ly = b:")
print(y)

print("\nSolution for x in Ux = y:")
print(x)
