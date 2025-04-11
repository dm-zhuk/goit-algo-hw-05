# Sorting algorithms

## The goal is to compare three sorting algorithms—Merge Sort, Insertion Sort, and Timsort—based on their runtime performance, and back this up with empirical data using Python’s timeit module.

## Analysis of Results

Tested Insertion Sort, Merge Sort, and Timsort on random, sorted, and reverse-sorted datasets (sizes: 100, 1000, 10000) using Python’s `timeit`.

### Random Data

- **100**: Insertion Sort (0.000244s), Merge Sort (0.000260s), Timsort (0.000018s)
- **1000**: Insertion Sort (0.037081s), Merge Sort (0.002510s), Timsort (0.000121s)
- **10000**: Insertion Sort (5.059977s), Merge Sort (0.038280s), Timsort (0.001461s)
- **Insight**: Insertion O(n²) scales poorly; Merge and Timsort O(n log n) are faster, with Timsort fastest.

### Sorted Data

- **100**: Insertion Sort (0.000015s), Merge Sort (0.000157s), Timsort (0.000004s)
- **1000**: Insertion Sort (0.000175s), Merge Sort (0.001841s), Timsort (0.000015s)
- **10000**: Insertion Sort (0.002018s), Merge Sort (0.025698s), Timsort (0.000206s)
- **Insight**: Insertion O(n) shows good speed; Merge Sort and Timsort (O(n log n)) are slower but efficient, Timsort best.

### Reverse-Sorted Data

- **100**: Insertion Sort (0.000493s), Merge Sort (0.000172s), Timsort (0.000007s)
- **1000**: Insertion Sort (0.073927s), Merge Sort (0.002022s), Timsort (0.000020s)
- **10000**: Insertion Sort (9.552948s), Merge Sort (0.025374s), Timsort (0.000176s)
- **Insight**: Insertion O(n²) worst-case struggles; Merge Sort and Timsort (O(n log n)) handle it well, Timsort No.1.

### Conclusion

- Insertion Sort: best for small/nearly sorted data, impractical for large/random (O(n²)).
- Merge Sort: consistent O(n log n) results across all cases.
- Timsort: Python’s hybrid (O(n log n)) outperforms both, optimized for real-world data.

### Test backup

Random Data:

Testing with 100 elements (random data):
Insertion Sort: 0.000244 seconds
Merge Sort: 0.000260 seconds
Timsort: 0.000018 seconds

Testing with 1000 elements (random data):
Insertion Sort: 0.037081 seconds
Merge Sort: 0.002510 seconds
Timsort: 0.000121 seconds

Testing with 10000 elements (random data):
Insertion Sort: 5.059977 seconds
Merge Sort: 0.038280 seconds
Timsort: 0.001461 seconds

Sorted Data:

Testing with 100 elements (sorted data):
Insertion Sort: 0.000015 seconds
Merge Sort: 0.000157 seconds
Timsort: 0.000004 seconds

Testing with 1000 elements (sorted data):
Insertion Sort: 0.000175 seconds
Merge Sort: 0.001841 seconds
Timsort: 0.000015 seconds

Testing with 10000 elements (sorted data):
Insertion Sort: 0.002018 seconds
Merge Sort: 0.025698 seconds
Timsort: 0.000206 seconds

Reverse Sorted Data:

Testing with 100 elements (reverse data):
Insertion Sort: 0.000493 seconds
Merge Sort: 0.000172 seconds
Timsort: 0.000007 seconds

Testing with 1000 elements (reverse data):
Insertion Sort: 0.073927 seconds
Merge Sort: 0.002022 seconds
Timsort: 0.000020 seconds

Testing with 10000 elements (reverse data):
Insertion Sort: 9.552948 seconds
Merge Sort: 0.025374 seconds
Timsort: 0.000176 seconds
