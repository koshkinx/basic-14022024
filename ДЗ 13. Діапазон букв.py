import string

input_str = input("Введите две буквы через дефис: ")

delit_defis = input_str.split('-')

start_index = string.ascii_letters.index(delit_defis[0])
end_index = string.ascii_letters.index(delit_defis[1])

substring = string.ascii_letters[start_index:end_index + 1]

print(substring)