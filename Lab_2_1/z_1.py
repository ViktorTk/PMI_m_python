"""Задача 1
Вам необходимо написать программу, которая рассчитывает сумму чисел ряда,
содержащего натуральные числа от 1 до n включительно. Однако в суммировании
участвуют только те числа, которые являются кратными 3 или содержат цифру 3 в
своей записи.

Входные данные:
На вход программа принимает одно целое число n (1 ≤ n ≤ 1000) """

def sum_of_special_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        # Проверяем, кратно ли число 3 или содержит ли цифру '3'
        if i % 3 == 0 or '3' in str(i):
            total_sum += i
    return total_sum

# Ввод значения perem_1, с проверкой на условие (1 ≤ n ≤ 1000)
perem_1 = int(input("Введите натуральное число: "))

if 1 <= perem_1 <= 1000: 
    result = sum_of_special_numbers(perem_1)
    print(f"Сумма чисел от 1 до {perem_1}, которые кратны 3 или содержат цифру 3: {result}")
else:
    print("Введенное число находится за пределами обозначенного диапазона: (1 ≤ n ≤ 1000)")

