# todo:
#     Напишите программу, которая определяет и печатает «похожие» слова. Слово называется похожим на другое слово,
#     если его гласные буквы находятся там же, где находятся гласные буквы другого слова, например:
#     дорога и пароход - похожие слова (гласные буквы на втором, четвертом и шестом местах),
#     станок и прыжок - похожие слова, питон и удав непохожие слова.
#     Считаем, что в русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е).
#     Ввод: x –первое слово, например, питон. n – количество слов для сравнения, например 6.
#     Дальше вводятся 6 слов, например: поросенок, титан, итог, лавка, погост, кино.
#     Вывод - слова, похожие на питон: титан, погост, кино


def get_same_words(word, num):
    vowels = 'аяеэёоуюиы'
    vowels_indexes = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_indexes.append(i)
    words = []
    for i in range(num):
        new_word = input()
        words.append(new_word)
    result = []
    for i in words:
        new_word_vowels_indexes = []
        for j in range(len(i)):
            if i[j] in vowels:
                new_word_vowels_indexes.append(j)
        if vowels_indexes == new_word_vowels_indexes:
            result.append(i)
    return ' '.join(result)


print(get_same_words('питон', 6))
