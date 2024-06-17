def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    current_row = range(m + 1)
    for i in range(1, n + 1):
        previous_row, current_row = current_row, [i] + [0] * m
        for j in range(1, m + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if s[j - 1] != t[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[m]

source = "yu"
target = "you"
print(f"Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")