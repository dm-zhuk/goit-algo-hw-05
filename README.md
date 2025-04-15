# Substring Search Algorithm Comparison

This project compares the efficiency of three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp on two text files. The goal is to measure execution time for finding an existing and a non-existing patterns using Python's `timeit` module.

## Methodology

- **Input Files**: Two text files (`article_1.txt`, `article_2.txt`) containing Ukrainian text.
- **Patterns**:
  - Existing: `"інтервал sqrt"` (present in both files).
  - Non-existing: `"nonexistent123"` (absent in both files).
- **Measurement**: Each algorithm was run 100 times per pattern per file using `timeit` to calculate average execution time.
- **Environment**: Python 3, macOS, standard Python libraries.

## Results

### Article 1

| Pattern      | Boyer-Moore | KMP      | Rabin-Karp |
| ------------ | ----------- | -------- | ---------- |
| Existing     | 0.037594    | 0.205965 | 0.260601   |
| Non-existing | 0.070780    | 0.380678 | 0.661640   |

### Article 2

| Pattern      | Boyer-Moore | KMP      | Rabin-Karp |
| ------------ | ----------- | -------- | ---------- |
| Existing     | 0.061871    | 0.360315 | 0.441064   |
| Non-existing | 0.097360    | 0.540614 | 0.971175   |

## Conclusion

Boyer-Moore outperformed KMP and Rabin-Karp in all cases, making it the most efficient for this task.

## Usage

1. Run `python3 main.py` to generate timing results.

## Backup data for Test 02

- **Processing article_1.txt:**

Existing pattern ('інтервал sqrt'):
Boyer-Moore: 0.054987 seconds
KMP: 0.188848 seconds
Rabin-Karp: 0.235622 seconds

Non-existing pattern ('nonexistent123'):
Boyer-Moore: 0.069103 seconds
KMP: 0.359402 seconds
Rabin-Karp: 0.573622 seconds

- **Processing article_2.txt:**

Existing pattern ('інтервал sqrt'):
Boyer-Moore: 0.057810 seconds
KMP: 0.321653 seconds
Rabin-Karp: 0.432857 seconds

Non-existing pattern ('nonexistent123'):
Boyer-Moore: 0.095727 seconds
KMP: 0.524034 seconds
Rabin-Karp: 0.853882 seconds
