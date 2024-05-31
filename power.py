import numpy as np

def power_method(matrix, initial_approximation, max_iterations=100, tolerance=1e-6):
    """
    Power Method for finding dominant eigenvalue and eigenvector
    :param matrix: Input matrix (numpy array)
    :param initial_approximation: Initial approximation for the eigenvector
    :param max_iterations: Maximum number of iterations
    :param tolerance: Convergence tolerance
    :return: Dominant eigenvalue and corresponding eigenvector
    """
    # Normalize the initial approximation
    x = initial_approximation / np.linalg.norm(initial_approximation)

    for i in range(max_iterations):
        # Power iteration
        y = np.dot(matrix, x)

        # Compute eigenvalue
        eigenvalue = np.dot(x, y)

        # Normalize eigenvector
        x = y / np.linalg.norm(y)

        # Print eigenvalue and eigenvector in each iteration
        print(f"Iteration {i + 1}: Eigenvalue = {eigenvalue}, Eigenvector = {x}")

        # Check for convergence
        if i > 0 and np.abs(eigenvalue - prev_eigenvalue) < tolerance:
            print(f"Converged at iteration {i + 1}")
            break

        prev_eigenvalue = eigenvalue

    return eigenvalue, x

# Get the order of the matrix from the user
order = int(input("Enter the order of the square matrix: "))

# Get individual elements of the matrix from the user
matrix_elements = []
for i in range(order):
    row_input = input(f"Enter elements for row {i + 1} (comma-separated): ")
    row_elements = list(map(float, row_input.split(',')))
    matrix_elements.append(row_elements)

# Convert the list of elements into a numpy array
matrix = np.array(matrix_elements)

# Get individual elements of the initial approximation from the user
initial_approximation_input = input("Enter the initial approximation for the eigenvector (comma-separated): ")
initial_approximation = np.array(list(map(float, initial_approximation_input.split(','))))

# Run power method
dominant_eigenvalue, dominant_eigenvector = power_method(matrix, initial_approximation)
print(f"\nDominant Eigenvalue: {dominant_eigenvalue}")
print(f"Dominant Eigenvector: {dominant_eigenvector}")
