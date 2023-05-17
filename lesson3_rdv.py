"""
Skypro. Профессия "Python-разработчик" ПОТОК
Урок 3. Списки и циклы. Домашнее задание 
Родительский Дмитрий Вячеславович
***** Часть 2. Задание со звездочкой ****
"""

# Вопросы и ответы пользователя
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# Слово для старта программы
MAGIC_WORD_TO_BEGIN = "ready"
# Количество попыток вводом пользователем ответов
USER_ATTEMPTS = 3

# Счетчики
# Правильные ответы пользователя
correct_user_answers = 0
# Количество набранных баллов
total_user_score = 0

# Начало работы программы

# НЕ допускаем ввода "пустого" ответа пользователем
while True:
    user_choice = (input(f"Привет! Предлагаю проверить свои знания английского! Наберите \"{MAGIC_WORD_TO_BEGIN}\", чтобы начать! ")).lower().strip()
    if user_choice != "": break

if user_choice == MAGIC_WORD_TO_BEGIN:
    # Начинаем наш цикл вопросов 
    for i in range(len(questions)):
        print(f"Вопрос № {i + 1}")
        print(questions[i])
        attempt = USER_ATTEMPTS
        # Считываем ответ пользователя
        user_answer = (input("Ваш ответ: ")).lower().strip()
        if user_answer == answers[i]:
            print("Ответ верный!")
            correct_user_answers += 1
            total_user_score += USER_ATTEMPTS
        #Неправильный ответ
        else:
            # Уменьшаем счетчик попыток ответа пользователя
            attempt -= 1
            for j in range(attempt):
                user_answer = (input(f"Осталось попыток: {attempt-j} попробуйте ещё раз >>> ")).lower().strip()
                if user_answer == answers[i]:
                    # Мы получили правильный ответ
                    print("Ответ верный!")
                    correct_user_answers += 1
                    total_user_score += (attempt-j)
                    break
            # Правильного ответа от пользователя так и не получили
            if user_answer != answers[i]: print(f"Увы, но нет. Верный ответ: {answers[i]}")

    print(f"Вот и всё! Вы ответили на {correct_user_answers} вопросов из {USER_ATTEMPTS} верно, вы набрали {total_user_score} баллов.")  
    
# Пользователь так и не введ нужное слово для начала теста 
else: print("Кажется, вы не хотите играть. Очень жаль.")

#########################
