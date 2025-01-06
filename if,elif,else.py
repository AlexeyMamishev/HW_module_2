first = input('введите 1-е чиcло: ')
second = input('введите 2-е чиcло: ')
third = input('введите 3-е чиcло: ')
if first == second == third:
    print('3')
elif first == second or first == third:
    print('2')
elif second == first or second == third:
    print('2')
elif third == first or third == second:
    print('2')
else:
    print('0')