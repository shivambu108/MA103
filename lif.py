def lagrange_interpolation(x_values, y_values, x):
    """
    Lagrange Interpolation
    :param x_values: List of x values
    :param y_values: List of corresponding y values
    :param x: The point at which to interpolate
    :return: Interpolated value at x
    """
    result = 0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


def inverse_lagrange_interpolation(x_values, y_values, y):
    """
    Find the x value for a given y using inverse Lagrange Interpolation
    :param x_values: List of x values
    :param y_values: List of corresponding y values
    :param y: The value for which to find the inverse
    :return: Inverse interpolated value at y
    """
    n = len(x_values)

    for i in range(n):
        if y_values[i] == y:
            return x_values[i]

    # If the exact value is not in the y_values, interpolate to find the inverse
    x_inverse = lagrange_interpolation(y_values, x_values, y)
    return x_inverse


# Example usage:
# Given data points
x_values = [1, 3, 4]
y_values = [4, 12, 19]

# Interpolation
interpolated_value = lagrange_interpolation(x_values, y_values, 2.5)
print(f"Interpolated value at x=2.5: {interpolated_value}")

# Inverse Interpolation
inverse_interpolated_value = inverse_lagrange_interpolation(x_values, y_values, 7)
print(f"Inverse interpolated value at y=9: {inverse_interpolated_value}")
