# Importing NumPy Library
import numpy as np
import sys

# Reading the number of unknowns
n = int(input('Enter the number of unknowns: '))

# Creating a numpy array of size n x n+1 for storing the augmented matrix
a = np.zeros((n, n+1))

# Creating a numpy array of size n for storing the solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input(f'a[{i}][{j}] = '))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
    for j in range(i+1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Backward Substitution
x[n-1] = a[n-1][n] / a[n-1][n-1]
for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - a[i][j] * x[j]
    x[i] = x[i] / a[i][i]

# Displaying the solution
print('\nRequired solution is:')
for i in range(n):
    print(f'X{i} = {x[i]:.2f}', end='\t')
