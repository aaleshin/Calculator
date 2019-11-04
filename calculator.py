#! /usr/bin/env python
# -*- coding: utf-8 -*-


def calculate():
    print('\tВы запустили калькулятор!!\n')
    count = 2
    while count < 11:
        try:
            number_1 = float(input('Введите первое число: '))
            operations = str(input(
                'Введите математическую операцию(Сложение(+), Вычитание(-), Произведение(*), Деление(/)): '))
            number_2 = float(input('Введите второе число: '))

        except ValueError:
            print("\n Вы ввели неверное значение! Попробуйте снова!")
            calculate()

        else:
            if operations == '+':
                count += 1
                result = number_1 + number_2
                print('Сумма чисел равна: ', result)

            elif operations == '-':
                result = number_1 - number_2
                print('Разность числе равна: ', result)
                count += 1

            elif operations == '*':
                result = number_1 * number_2
                print('Произведение числе равно: ', result)
                count += 1

            elif operations == '/' and number_2 == 0:
                print('делить на 0 нельзя!')
                continue

            elif operations == '/' and number_2 != 0:
                result = number_1 / number_2
                print('Деление чисел равно: ', result)
                count += 1

            else:
                print('Вы ввели не поддрерживаемую математическую операцию!')
                calculate()

            # new_result += result
            s = input('Ввести еще 1 значение? (Y/N): ')
            if s.upper() == 'Y':
                print()
                # print('Текущий результат:', new_result)

            elif s.upper() == 'N':
                # final_result = new_result + result
                # print('Программа завершена! Итоговый результат: ', final_result)
                print('Количество введенных чисел равно:', count)
                count = 11

            else:
                calculate()


calculate()

# Необходимо решить проблему с счетчиком и итогового результата. Так же добавить ограничения на отрицательные  числа.