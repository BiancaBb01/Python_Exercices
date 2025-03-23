def compare_dicts(d1, d2):
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            return False
        return all(compare_dicts(d1[k], d2[k]) for k in d1)
    elif isinstance(d1, list) and isinstance(d2, list):
        if len(d1) != len(d2):
            return False
        return all(compare_dicts(a, b) for a, b in zip(d1, d2))
    elif isinstance(d1, set) and isinstance(d2, set):
        return d1 == d2
    else:
        return d1 == d2

# Example usage
dict1 = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4]
    },
    "e": {5, 6}
}

dict2 = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4]
    },
    "e": {6, 5}
}

print(compare_dicts(dict1, dict2))  # Output: True
