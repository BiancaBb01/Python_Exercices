def count_unique_and_duplicates(lst):
    unique_elements = set()
    duplicates_seen = set()
    duplicate_count = 0

    for item in lst:
        if item in unique_elements:
            if item not in duplicates_seen:
                duplicates_seen.add(item)
                duplicate_count += 1
        else:
            unique_elements.add(item)

    unique_count = len(unique_elements)

    return (unique_count, duplicate_count)


# Exemplu de utilizare
example_list = [1, 2, 3, 4, 5, 5, 6, 7]
result = count_unique_and_duplicates(example_list)
print(result)  # Output: (7, 2)
