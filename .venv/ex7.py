def set_operations(*sets):
    result = {}
    sets = list(sets)

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i], sets[j]
            result[f"{a} | {b}"] = a | b
            result[f"{a} & {b}"] = a & b
            result[f"{a} - {b}"] = a - b
            result[f"{b} - {a}"] = b - a

    return result


# Example usage
s1 = {1, 2}
s2 = {2, 3}

result = set_operations(s1, s2)
for k, v in result.items():
    print(f"{k}: {v}")

# Output:
# {1, 2} | {2, 3}: {1, 2, 3}
# {1, 2} & {2, 3}: {2}
# {1, 2} - {2, 3}: {1}
# {2, 3} - {1, 2}: {3}
