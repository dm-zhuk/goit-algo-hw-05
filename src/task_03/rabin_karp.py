# Implement the Rabin-Karp algorithm
def rabin_karp(text, pattern):
    m = len(pattern)
    n = len(text)
    d = 256  # Char number in the input alphabet
    q = 101  # Prime number
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i  # Pattern found

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1  # Pattern not found
