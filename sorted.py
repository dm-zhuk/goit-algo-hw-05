import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Timsort (using Python's built-in sorted)
def timsort(arr):
    return sorted(arr)


def generate_test_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(1, 10000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse":
        return list(range(size, 0, -1))


# Test function
def test_sorting_algorithms(sizes, data_type="random"):
    for size in sizes:
        data = generate_test_data(size, data_type)
        print(f"\nTesting with {size} elements ({data_type} data):")

        # Insertion Sort
        time_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        print(f"Insertion Sort: {time_insertion:.6f} seconds")

        # Merge Sort
        time_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        print(f"Merge Sort: {time_merge:.6f} seconds")

        # Timsort
        time_timsort = timeit.timeit(lambda: timsort(data.copy()), number=1)
        print(f"Timsort: {time_timsort:.6f} seconds")


# Run tests
sizes = [100, 1000, 10000]
print("\nRandom Data:")
test_sorting_algorithms(sizes, "random")
print("\nSorted Data:")
test_sorting_algorithms(sizes, "sorted")
print("\nReverse Sorted Data:")
test_sorting_algorithms(sizes, "reverse")
