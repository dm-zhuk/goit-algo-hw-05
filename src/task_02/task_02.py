"""
Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.
"""


def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]
        else:
            return (iterations, arr[mid])  # Target found

    # If target not found, determine upper bound
    if low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)


# Test the function
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
x_value = 7.0

result = binary_search(sorted_array, x_value)
print(result)  # (3, 7.7)
