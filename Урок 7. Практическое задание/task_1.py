"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import Timer
RND_LIST_1 = [randint(-100, 100) for _ in range(1000)]
RND_LIST_2 = [randint(-100, 100) for _ in range(1000)]


def bubble_1(my_list):
    """Простая сортировка пузырьком"""
    for _ in range(len(my_list)):
        for i in range(len(my_list)-1):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


def bubble_2(my_list):
    """Улучшеная сортировка пузырьком"""
    for _ in range(len(my_list)):
        complete = True
        for i in range(len(my_list)-1):
            if my_list[i] < my_list[i + 1]:
                complete = False
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        if complete:
            break
    return my_list


T1 = Timer("bubble_1(RND_LIST_1)", "from __main__ import bubble_1, RND_LIST_1")
T2 = Timer("bubble_2(RND_LIST_2)", "from __main__ import bubble_2, RND_LIST_2")
print(f"Список случайных чисел после обычного варианта сортировки:"
      f"\n{bubble_1(RND_LIST_1)}\nСортировка заняла: {T1.timeit(number=10)}")
print(f"Список случайных чисел после улучшенного варианта сортировки:"
      f"\n{bubble_2(RND_LIST_2)}\nСортировка заняла: {T2.timeit(number=10)}")
