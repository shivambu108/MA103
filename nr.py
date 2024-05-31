# Defining the nonlinear function f(x)
def f(x):
    return (x + 15/x )/2

# Defining the derivative of the function
def f_prime(x):
    return 2*x

# Implementing the Newton-Raphson Method
def newton_raphson(x0, e, N):
    print("\n\n*** NEWTON-RAPHSON METHOD IMPLEMENTATION ***")
    step = 1
    flag = 1
    condition = True
    while condition:
        if f_prime(x0) == 0.0:
            print("Divide by zero error!")
            break
        x1 = x0 - f(x0) / f_prime(x0)
        print(f"Iteration-{step}, x1 = {x1:.6f}, f(x1) = {f(x1):.6f}")
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

# Starting the Newton-Raphson Method
newton_raphson(x0, e, N)
