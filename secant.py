import numpy as np
# Defining the function f(x)
def f(x):
    return x*np.e**x -1 

# Implementing the Secant Method
def secant(x0, x1, e, N):
    print("\n\n*** SECANT METHOD IMPLEMENTATION ***")
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print("Divide by zero error!")
            break
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print(f"Iteration-{step}, x2 = {x2:.5f} and f(x2) = {f(x2):.5f}")
        x0 = x1
        x1 = x2
        step += 1
        if step > N:
            print("Not Convergent!")
            break
        condition = abs(f(x2)) > e

    print(f"\nRequired root is: {x2:.5f}")

# Input Section
x0 = float(input("Enter First Guess: "))
x1 = float(input("Enter Second Guess: "))
e = float(input("Tolerable Error: "))
N = int(input("Maximum Step: "))

# Starting the Secant Method
secant(x0, x1, e, N)

