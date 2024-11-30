"""  Задача 5: Работа с текстовыми данными и анализ частоты слов
 Напишите программу, которая:
 1. Принимает на вход текст, состоящий из нескольких предложений.
 2. Разделяет текст на слова, игнорируя знаки препинания.
 3. Определяет и выводит 5 самых часто встречающихся слов в тексте, а также
 количество их вхождений.
 4. Находит и выводит самое длинное слово в тексте.
 5. Проверяет, содержатся ли в тексте все гласные буквы (а, е, ё, и, о, у, ы, э, ю, я).
 6. Если текст состоит из более чем 10 предложений, программа должна вывести
 первые 3 предложения и последние 3 предложения текста """



import re
from collections import Counter

def analyze_text(text):
    # Разделяем текст на слова, игнорируя знаки препинания
    words = re.findall(r'\b\w+\b', text.lower())

    # Определяем 5 самых частых слов
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(5)

    # Находим самое длинное слово
    longest_word = max(words, key=len)

    # Проверяем наличие всех гласных букв
    vowels = set("аеёиоуыэюя")
    has_all_vowels = vowels.issubset(set(''.join(words)))

    # Работа с предложениями
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    output = {
        "most_common_words": most_common_words,
        "longest_word": longest_word,
        "has_all_vowels": has_all_vowels
    }

    if len(sentences) > 10:
        output["sentences_preview"] = {
            "first_3": sentences[:3],
            "last_3": sentences[-3:]
        }

    return output

# Пример ввода

# text = """Ра́йан То́мас Го́слинг (англ. Ryan Thomas Gosling, род. 12 ноября 1980, Лондон, Онтарио, Канада) — канадский актёр.
# Известен по ролям в независимых фильмах и крупных студийных проектах разных жанров. Сборы фильмов с его участием составили свыше 1,9 миллиарда долларов.
# Обладатель многих наград[англ.], включая «Золотого глобуса», и номинант трёх «Оскаров» и одного BAFTA.
# Гослинг родился и вырос в Канаде. Обрёл известность в 13 лет как ребёнок-актёр в программе телеканала Disney Channel «Клуб Микки Мауса» и появился в нескольких
# семейных передачах, в том числе «Боишься ли ты темноты?», «Мурашки» и «На волне успеха». Прорывом стала роль еврейского неонациста в фильме «Фанатик»,
# а в романтической драме «Дневник памяти» Гослинг завоевал славу."""


text = str(input("Введите нужный вам текст: "))


result = analyze_text(text)

# Вывод результатов
print("Самые частые слова:")
for word, count in result["most_common_words"]:
    print(f"{word}: {count}")

print("\nСамое длинное слово:", result["longest_word"])
print("\nВсе гласные присутствуют:", "Да" if result["has_all_vowels"] else "Нет")

if "sentences_preview" in result:
    print("\nПервые 3 предложения:")
    for sentence in result["sentences_preview"]["first_3"]:
        print(sentence)

    print("\nПоследние 3 предложения:")
    for sentence in result["sentences_preview"]["last_3"]:
        print(sentence)






