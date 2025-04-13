# Implement the Boyer-Moore algorithm
def boyer_moore(text, pattern):
    # Preprocessing pattern
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i

    m = len(pattern)
    n = len(text)
    s = 0

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s  # Pattern found

        s += j - bad_char.get(text[s + j], -1)

    return -1  # Pattern not found
