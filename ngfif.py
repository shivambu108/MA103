def newton_forward_interpolation(x_values, y_values, target_x):
    n = len(x_values)
    
    # Calculate forward difference coefficients
    forward_difference_coefficients = [y_values]

    for j in range(1, n):
        temp_coefficients = []
        for i in range(n - j):
            temp_coefficients.append((forward_difference_coefficients[j - 1][i + 1] - forward_difference_coefficients[j - 1][i]) / (x_values[i + j] - x_values[i]))
        forward_difference_coefficients.append(temp_coefficients)
    
    # Calculate the interpolated value using the forward difference coefficients
    result = y_values[0]
    temp_product = 1
    
    for j in range(1, n):
        temp_product *= (target_x - x_values[j - 1])
        result += (forward_difference_coefficients[j][0] * temp_product)
    
    return result

# Example usage:
x_values = [0, 1, 2, 3, 4]
y_values = [1, 2, 8, 26, 80]
target_x = 2.5

result = newton_forward_interpolation(x_values, y_values, target_x)
print(f"The interpolated value at x = {target_x} is: {result}")
