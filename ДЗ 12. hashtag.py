#ДЗ 12. hashtag

import string

input_str = input("Введите строку: ")

cleaned_str = ''
for char in input_str:
    if char not in string.punctuation:
        cleaned_str += char

words = cleaned_str.split()

hashtag = '#'
for word in words:
    hashtag += word.capitalize()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print("Хештег:", hashtag)