def sorter(a):
    if int(a) % 2 == 0:
        print(f'Число {a} четное')
    else:
        print(f'Число {a} нечетное')
while True:
    b = input('введи число: ')
    sorter(b)