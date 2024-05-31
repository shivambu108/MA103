import numpy as np

def gauss_jacobi(A, b, initial_guess, max_iterations=50, tolerance=1e-6):
    n = len(b)
    x = np.copy(initial_guess)
    
    print("\nGauss-Jacobi Method:")
    for iteration in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            sigma = np.dot(A[i, :i], x_old[:i]) + np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]
        
        print(f"Iteration {iteration + 1}: {x}")
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            print("\nConverged!")
            break
    else:
        print("\nDid not converge within the maximum number of iterations.")

def gauss_seidel(A, b, initial_guess, max_iterations=50, tolerance=1e-6):
    n = len(b)
    x = np.copy(initial_guess)
    
    print("\nGauss-Seidel Method:")
    for iteration in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]
        
        print(f"Iteration {iteration + 1}: {x}")
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            print("\nConverged!")
            break
    else:
        print("\nDid not converge within the maximum number of iterations.")

def main():
    # User input for the system of equations
    n = int(input("Enter the number of variables: "))
    A = np.zeros((n, n))
    b = np.zeros(n)

    print("\nEnter the coefficients of the system of equations:")
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"Coefficient A[{i+1},{j+1}]: "))
        b[i] = float(input(f"Constant b[{i+1}]: "))

    initial_guess = np.zeros(n)
    for i in range(n):
        initial_guess[i] = float(input(f"Enter initial guess for x[{i+1}]: "))

    method = input("\nEnter the method (1 for Gauss-Jacobi, 2 for Gauss-Seidel): ")

    if method == '1':
        gauss_jacobi(A, b, initial_guess)
    elif method == '2':
        gauss_seidel(A, b, initial_guess)
    else:
        print("Invalid method selection. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
