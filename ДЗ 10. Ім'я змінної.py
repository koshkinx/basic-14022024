import keyword
import string

name = input("Введите имя переменной: ")
if name[0].isdigit():
    print(False)
    exit()

for char in name:
    if char in string.punctuation and char != '_':
        print(False)
        exit()
    if char.isupper():
        print(False)
        exit()

if name in keyword.kwlist:
    print(False)
    exit()

if name.count('_') == 1 and len(name) > 1:
    print(True)
    exit()

print(True)