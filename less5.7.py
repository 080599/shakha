allproduct = {'ves" sklad': {}}
korzina = []
admin = input('sto xotite sdelat"')
prname = input()
prcount = input()
allproduct['ves" skald'][prname] = prcount
print(allproduct)
chtokupit = input()
print(korzina)
if prname in allproduct:
        if prname in korzina:
            korzina[prname] += prcount
        else:
            korzina[prname] = prcount
        print(f"{prcount} {prname}(ов) добавлено в корзину.")
else:
        print("Товар не найден.")
if korzina:
        print("Ваша корзина:")
        for product, prcount in korzina.items():
            print(f"{prcount} x {product}")
else:
    print("Ваша корзина пуста.")
while True:
        action = input("Введите 'добавить' для добавления продукта или 'продукты' для просмотра корзины: ")

        if action.lower() == "добавить":
            prname = input("Введите название товара: ")
            prcount = int(input("Введите количество: "))
            korzina.append(prname,prcount)
        elif action.lower() == "продукты":
            print(korzina)
        else:
            print("Неверный ввод.")