#! /usr/bin/env python
# -*- coding: utf-8 -*-


def input_num(input_text):
    while True:
        try:
            number = float(input(input_text))
            if number < 0:
                print('Вы ввели отрицательное значение! Введите положительное.')
                continue
            break
        except ValueError:
            print(" Вы ввели неверное значение! Попробуйте снова!\n")

    return number


def input_op(input_text):
    operations_list = ('+', '-', '*', '/')
    while True:
        operation = input(input_text)
        if operation in operations_list:
            break
        print('Вы ввели не поддрерживаемую математическую операцию!\n')

    return operation


def calculate(number_1, count):
    result = 0
    while count < 11:
        operations = input_op(
            'Введите математическую операцию(Сложение(+), Вычитание(-), Произведение(*), Деление(/)): ')
        number_2 = input_num('Введите следующее число: ')

        if operations == '+':
            result = number_1 + number_2
            print('Сумма чисел равна: ', result)
            count += 1

        if operations == '-':
            result = number_1 - number_2
            print('Разность чисел равна: ', result)
            count += 1

        if operations == '*':
            result = number_1 * number_2
            print('Произведение числе равно: ', result)
            count += 1

        if operations == '/':
            while number_2 == 0:
                print('делить на 0 нельзя!')
                number_2 = input_num('Введите другое число не равное 0!:')
            result = number_1 / number_2
            print('Деление чисел равно: ', result)
            count += 1

        s = input('Ввести еще 1 значение? (Y/N): ')
        if s.upper() == 'Y':
            calculate(result, count)

        else:
            print('\nПрограмма завершена! Итоговый результат: ', result)
            print('Количество введенных чисел равно:', count)
        break


print('\tВы запустили калькулятор!!\n')
first_number = input_num('Введите первое число: ')
calculate(first_number, 1)
