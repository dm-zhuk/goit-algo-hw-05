"""
Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.
"""

import timeit
from boyer_moore import boyer_moore
from kmp import kmp
from rabin_karp import rabin_karp


def compare_algorithms(file1, file2, existing_substring, non_existing_substring):
    with open(file1, "r", encoding="utf-8") as f:
        text1 = f.read()
    with open(file2, "r", encoding="utf-8") as f:
        text2 = f.read()

    algorithms = {"Boyer-Moore": boyer_moore, "KMP": kmp, "Rabin-Karp": rabin_karp}

    results = {}

    for algorithm_name, algorithm in algorithms.items():
        for text_name, text in zip(["Article 1", "Article 2"], [text1, text2]):
            time_existing = timeit.timeit(
                lambda: algorithm(text, existing_substring), number=1000
            )
            time_non_existing = timeit.timeit(
                lambda: algorithm(text, non_existing_substring), number=1000
            )
            results[(algorithm_name, text_name)] = (time_existing, time_non_existing)

    return results


# Test the algorithms with two text files
existing_substring = "алгоритмів"  # Adjust this to a real substring in the texts
non_existing_substring = "вигаданий_підрядок"  # Adjust this to a made-up substring
results = compare_algorithms(
    "article_1.txt", "article_2.txt", existing_substring, non_existing_substring
)

for key, value in results.items():
    print(
        f"{key[0]} in {key[1]}: Existing time = {value[0]:.6f}s, Non-existing time = {value[1]:.6f}s"
    )
