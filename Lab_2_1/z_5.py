"""Задача 5
Напишите программу, которая находит число с максимальной суммой цифр в
диапазоне от p до q включительно. Диапазон задается целыми числами p и q (1 ≤ p ≤ q
≤ 1000). Если несколько чисел имеют одинаковую максимальную сумму цифр,
выведите наименьшее из них.

Входные данные:
На вход подаются два целых числа p и q.

Выходные данные:
Программа должна вывести одно целое число — число с максимальной суммой цифр. """

def argumentSum(a):
    # Преобразуем число в строку, разбиваем на отдельные символы и затем конвертируем в целые числа
    digits = [int(digit) for digit in str(a)]
    # Возвращаем сумму цифр
    return sum(digits)

# Ввод данных
p = int(input("Введите первое целое число "))
q = int(input("Введите второе целое число "))


# Нахождение числа с максимальной суммой цифр
result_p = argumentSum(p)
result_q = argumentSum(q)

# Вывод результата
if 1 <= p <= q <= 1000:
    print(f"сумма всех чисел {p} = {result_p}")
    print(f"сумма всех чисел {q} = {result_q}")
    if result_p > result_q:
        print(f"сумма всех чисел внутри {p} больше суммы всех чисел внутри {q}, и равняется {result_p}")
    else:
        print(f"сумма всех чисел внутри {q} больше суммы всех чисел внутри {p}, и равняется {result_q}")
else:
    print("Введите числа, соответствующие условиям (1 ≤ p ≤ q≤ 1000)")

