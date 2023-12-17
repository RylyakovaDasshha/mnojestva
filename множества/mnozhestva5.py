with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()  

words = text.split()  # Разбиваем текст на слова 

unique_words = set(words)  # определениe уникальных слов
count_unique_words = len(unique_words)  # Считаем количество уникальных слов

print("Количество различных слов в тексте:", count_unique_words)
