word_set = set()
with open("input.txt","r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            word_set.add(word)

number_of_words = len(word_set)
print("Количество разных слов в тексте:", number_of_words)
