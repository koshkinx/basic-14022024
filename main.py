def popular_words(text, words):
    # Приводим текст к нижнему регистру
    text_lower = text.lower()
    # Разбиваем текст на слова
    text_words = text_lower.split()
    # Создаем словарь для подсчета популярности слов
    word_count = {word: 0 for word in words}
    # Подсчитываем количество вхождений каждого слова из списка в тексте
    for word in text_words:
        if word in word_count:
            word_count[word] += 1
    return word_count

# Проверка
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')