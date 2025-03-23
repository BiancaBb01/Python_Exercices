def my_function(*args, **kwargs):
    count = 0
    kwargs_values = set(kwargs.values())
    for arg in args:
        if arg in kwargs_values:
            count += 1
    return count

# Example usage
result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)  # Output: 3
