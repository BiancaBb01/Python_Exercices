def char_frequency(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Example usage
text = "Ana has apples."
result = char_frequency(text)
print(result)
