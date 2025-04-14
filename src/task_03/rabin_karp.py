# Implement the Rabin-Karp algorithm
def rabin_karp(text, pattern):
    if not pattern or not text:
        return -1
    d = 256
    q = 101
    m, n = len(pattern), len(text)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1
