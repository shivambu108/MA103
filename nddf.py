def divided_difference(x_values, y_values):
    n = len(x_values)
    coefficients = [y_values]

    for j in range(1, n):
        temp_coefficients = []
        for i in range(n - j):
            temp_coefficients.append((coefficients[j - 1][i + 1] - coefficients[j - 1][i]) / (x_values[i + j] - x_values[i]))
        coefficients.append(temp_coefficients)

    return coefficients

def newton_divided_difference_interpolation(x_values, y_values, target_x):
    n = len(x_values)
    coefficients = divided_difference(x_values, y_values)

    result = coefficients[0][0]
    temp_product = 1

    for j in range(1, n):
        temp_product *= (target_x - x_values[j - 1])
        result += (coefficients[j][0] * temp_product)

    return result

# Example usage:
x_values = [0, 1, 2, 3, 4]
y_values = [1, 2, 8, 26, 80]
target_x = 2.5

result = newton_divided_difference_interpolation(x_values, y_values, target_x)
print(f"The interpolated value at x = {target_x} is: {result}")
