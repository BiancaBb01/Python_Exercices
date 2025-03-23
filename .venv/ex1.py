def list_operations(a, b):
    a_set, b_set = set(a), set(b)

    # Calculate the required sets
    intersected = a_set & b_set
    reunited = a_set | b_set
    a_minus_b = a_set - b_set
    b_minus_a = b_set - a_set

    return [intersected, reunited, a_minus_b, b_minus_a]


# Example usage
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = list_operations(a, b)
print(result)  # Output: [{3, 4}, {1, 2, 3, 4, 5, 6}, {1, 2}, {5, 6}]
