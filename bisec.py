# Defining the nonlinear function f(x)
def f(x):
    return x**3 - 4*x - 9

# Implementing the Bisection Method
def bisection(a, b, e):
    step = 1
    print("\n\n*** BISECTION METHOD IMPLEMENTATION ***")
    condition = True
    while condition:
        xi = (a + b) / 2
        f_a = f(a)
        f_b = f(b)
        f_xi = f(xi)
        sign_change = "+" if f_a * f_xi < 0 else "-"
        
        print(f"Iteration-{step}:")
        print(f"    a = {a:.5f}, b = {b:.5f},  f(a) = {f_a:.5f}, f(b) = {f_b:.5f}, xi = {xi:.5f}, f(xi) = {f_xi:.5f}, Sign Change: {sign_change}")
        

        if f_a * f_xi < 0:
            b = xi
        else:
            a = xi
        step += 1
        condition = abs(f_xi) > e

    print(f"\nRequired Root is: {xi:.5f}")

# Input Section
a = float(input("Enter the initial value of a: "))
b = float(input("Enter the initial value of b: "))
e = float(input("Enter the tolerable error (e): "))

# Checking correctness of initial guess values and bisecting
if f(a) * f(b) > 0.0:
    print("Given guess values do not bracket the root.")
    print("Try again with different guess values.")
else:
    bisection(a, b, e)



