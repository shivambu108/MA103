# Defining the nonlinear function f(x)
def f(x):
    return x**3 - 5*x - 9

# Implementing the Regula Falsi Method
def regula_falsi(a, b, e, N):
    print("\n\n*** REGULA FALSI METHOD IMPLEMENTATION ***")
    step = 1
    condition = True
    while condition:
        if f(a) == f(b):
            print("Divide by zero error!")
            break
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"Iteration-{step}, c = {c:.6f} and f(c) = {f(c):.6f}")
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        step += 1
        condition = abs(f(c)) > e and step <= N

    print(f"\nRequired root is: {c:.8f}")

# Input Section
a = float(input("Enter the first guess (a): "))
b = float(input("Enter the second guess (b): "))
e = float(input("Tolerable Error: "))
N = int(input("Maximum Iterations: "))

# Starting the Regula Falsi Method
regula_falsi(a, b, e, N)
