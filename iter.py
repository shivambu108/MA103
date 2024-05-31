# Importing math to use sqrt function
import math

# Define the nonlinear function f(x)
def f(x):
    return x**3 + x**2 - 1

# Re-write f(x) = 0 to x = g(x)
def g(x):
    return 1 / math.sqrt(1 + x)

# Implement the Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print("\n\n*** FIXED POINT ITERATION ***")
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print(f"Iteration-{step}, x1 = {x1:.5f} and f(x1) = {f(x1):.5f}")
        x0 = x1
        step += 1
        if step > N:
            flag = 0
            break
        condition = abs(f(x1)) > e

    if flag == 1:
        print(f"\nRequired root is: {x1:.5f}")
    else:
        print("\nNot Convergent.")

# Input Section
x0 = float(input("Enter Guess: "))
e = float(input("Tolerable Error: "))
N = int(input("Maximum Step: "))

# Starting Fixed Point Iteration Method
fixedPointIteration(x0, e, N)
