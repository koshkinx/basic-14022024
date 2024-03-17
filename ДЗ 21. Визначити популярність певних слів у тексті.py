def popular_words(text, words):
    text_lower = text.lower()
    words_list = text_lower.split()
    word_count = {}
    for word in words:
        count = 0
        for text_word in words_list:
            if text_word == word:
                count += 1
        word_count[word] = count
    return word_count

# Перевірка
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
result = popular_words('When I was One I had just begun When I was Two I was nearly new', ['i', 'was', 'three', 'near'])
print(result)