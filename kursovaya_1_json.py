"""
Skypro. Профессия "Python-разработчик" ПОТОК
Курсовая работа по курсу № 1
Родительского Дмитрия Вячеславовича
"""
import random
import json

# Количество впоросов для тестирования пользователя
TOTAL_ANSWERS = 5

# Для отключения отладочных сообщений
DEBUG = bool(1)

def print_statistics(user_answers):
    """
    Выводит статистику ответов пользователя
    """
    total_answers = len(user_answers)
    total_right_answers = user_answers.count(True)
    print(f"Всего задачек: {total_answers}")
    print(f"Отвечено верно: {total_right_answers}")
    print(f"Отвечено неверно: {total_answers - total_right_answers}")

    
def get_random_word(words):
    """
    Выводит случайное слово из передаваемого списка
    Также преобразует это слово к нижнему регистру
    """
    return str((random.choice(words)).lower())


def morse_encode(morse_list, words_to_encode):
    """
    Функция преобразует введенное пользователем слов в нижний регистр
    затем кодирует его по системе Морзе и возращает в виде строки
    В функцию передаем ссылку на ранее созданный словарь со значением
    символов и соотвествующих им кодов Морзе
    """
    return (" ".join([morse_list[i] for i in words_to_encode])).strip()

# Список слов для проверки пользователя
word_list = ["bird", "tree", "freedom", "random", "timer", 
              "magic", "power", "glory", "seed", "beauty", "grafana",
              "flower", "reader", "writer", "save", "spirit", "traffic",
              "heart", "friend", "queen", "innuendo", "rapsody",
              "trip", "type", "python", "pascal", "ruby", "Welcome",
              "morning", "day", "moon", "west", "north", "east", "south",
              "god", "kingthom", "swap", "linux", "pray", "Salt", "unix", 
              "FreeBSD", "OpenBSD", "FreeNas", "Debian", "pillow", "capital", "tower", 
              "user", "Snake", "security", "setting", "kernel", "release", "module", 
              "edit", "selection", "ordinary", "terminal", "zabbix", "repo"]

# Список для хранения ответов пользователя
answers = []

# # Готовим словарь кодов Морзе

def get_morse_dict():
    """
    Загружаем словарь с кодами Морзе зи JSON-файла
    """
    with open('morse-code.json') as json_file:
        data = json.load(json_file)
    
    return data


def main():
    """
    Основная функция приложения
    """
    # Загружаем коды Морзе 
    morse_code = get_morse_dict()

    # Выводим сообщение пользователю
    print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
    input("Нажмите Enter и начнем ")

    # Выводим список слов для тестирования пользователя
    # в количестве TOTAL_ANSWERS раз
    for number in range(TOTAL_ANSWERS):
    #Получаем слово для тестирования пользователя
        user_test_word = get_random_word(word_list)
        template_morse_word = (morse_encode(morse_code, user_test_word)).strip()
        # Для тестирования выводим правильное слово
        if DEBUG: print(f"Случайное слово № {number + 1} из списка >>> {user_test_word}")
        print(f"Слово {number + 1} >>> {template_morse_word}")
        # Исключаем пустой ввод пользователя
        while True:
            user_variant = input("Введите Ваш вариант: ").lower().strip()
            if user_variant != "": break
        """
        Обработка правильного и неправильного вариантов ввода пользователя
        """
        if user_variant == user_test_word:
            print(f"Верно, {user_variant} !")
            answers.append(True)
        else:
            print(f"Неверно, {user_test_word} !")
            answers.append(False)

    # Выводим статистику работы пользователя
    print_statistics(answers)


# Тело работы приложения
if __name__ == "__main__":
    main()

#########


    
