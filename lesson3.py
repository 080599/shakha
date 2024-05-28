word=input("Введите слово-")
word = word.lower().replace(" ", "")
if word == word[::-1]:
    print(f"{word} является палиндромом.")
else:
    print(f"{word} не является палиндромом.")

