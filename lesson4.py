"""
Skypro. Профессия "Python-разработчик" ПОТОК
Урок 4. Строки и словари. Домашнее задание 
Родительский Дмитрий Вячеславович
"""

# Основные объекты
# Словари для тестирования знаний
# по разным уровням
words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

# Словарь уровней знаний пользователя
levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

# Динамический словарь для записи ответов юзверя
# в виде пары {Слово для перевода : ответ пользователя (верный/неверный)}
answers = {}

# Начало программы

# Уровень доступа пользователя
user_level = ""

# Список уровней пользователя
user_levels = ["легкий", "средний", "сложный"]


while user_level not in user_levels:
    user_level = input("Выберете уровень сложности:\nЛегкий, средний, сложный: ").lower().strip()

# Подключаем словарь для работы с пользователем
if user_level == user_levels[0]: words = words_easy
elif user_level == user_levels[1]: words = words_medium
else: words = words_hard

print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод. ")

# Перебираем наш словарь
for key in words:
    # перебираем словарб по ключам -- словам на английском языке
    # key - слово на английском языке, words[key] или words.get(key) - значение словаря - слово на русском
    user_answer = input(f"{str(key).capitalize()}, {len(str(words[key]))} букв, начинатеся с {words[key][0]}... ").lower().strip()
    if user_answer == words[key]:
        print(f"Верно. {str(key).capitalize()} - это {words[key]}.")
        answers[key] = True
    else:
        print(f"Неверно. {str(key).capitalize()} - это {words[key]}.")
        answers[key] = False
   
# Выводим итоговые результаты работы
# Взводим флаг для подавлений вывода пустой положительной статистики
is_first = True
# Выводим правильные ответы пользователя
for key in answers:
    if answers[key] == True: 
        if is_first:
            is_first = False
            print("Правильно отвечены слова:" )
        print(key)

# Взводим флаг для подавлений вывода пустой отрицательной статистики
is_first = True
# Выводим неправильные ответы пользователя
for key in answers:
    if answers[key] == False: 
        if is_first:
            is_first = False
            print("Неправильно отвечены слова:" )
        print(key)

# Получаем лист значений (ИСТИНА-ЛОЖЬ) для определения ранга ползователя
check_list = list(answers.values())

#Выводим ранг пользователя
print("Ваш ранг:")
print(levels[check_list.count(True)])

##################
