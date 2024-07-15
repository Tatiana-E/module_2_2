first = input('Введите любое число: ')
second = input('Введите любое число: ')
third = input('Введите любое число: ')
if first == second and second == third:  # или if first == second == second == third
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)