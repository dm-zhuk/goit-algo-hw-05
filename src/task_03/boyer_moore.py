# Implement the Boyer-Moore algorithm
def boyer_moore(text, pattern):
    if not pattern or not text:
        return -1

    m = len(pattern)
    n = len(text)

    # Initialize bad character table
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s  # Pattern found

        # Get shift for bad character
        char = text[s + j] if s + j < n else None
        if char is None or s + j >= n:
            return -1  # Prevent out-of-bounds
        shift = bad_char.get(char, -1)
        s += max(1, j - shift)

    return -1  # Pattern not found
