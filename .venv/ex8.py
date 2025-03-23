def find_loop(mapping):
    visited = set()
    result = []
    current_key = 'start'

    while current_key not in visited:
        visited.add(current_key)
        current_value = mapping[current_key]
        result.append(current_value)
        current_key = current_value

    # Oprim inainte de a adauga elementul care ar crea bucla
    if result[-1] in visited:
        result.pop()

    return result

# Examplu
mapping = {
    'start': 'a',
    'b': 'a',
    'a': '6',
    '6': 'z',
    'x': '2',
    'z': '2',
    '2': '2',
    'y': 'start'
}

print(find_loop(mapping))  # Output: ['a', '6', 'z', '2']
