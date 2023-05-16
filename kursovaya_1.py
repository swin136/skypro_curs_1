"""
Курсовая работа по курсу № 1
Родительского Дмитрия Вячеславовича
"""
import random

# Количество впоросов для тестирования пользователя
TOTAL_ANSWERS = 5

# Для отключения отладочных сообщений
DEBUG = bool(0)

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
    символов и соотвествующих им кодар Морзе
    """
    user_word = list(words_to_encode.lower())
    morse = ""
    for j in range(len(user_word)):
        if j == 0:
            morse = morse_code.get(user_word[j])  
        else:
           morse = morse + " " + morse_code.get(user_word[j])   
    return str(morse)

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
              "edit", "selection", "ordinary", "terminal", "zabbix"]

# Список для хранения ответов пользователя
answers = []

# Готовим словарь кодов Морзе

morse_symbols = ["0", "1", "2", "3", "4", "5", "6",  "7", "8", "9",
                 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q",  "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", ".",  ",", "?", "!",
                 "-", "/", "@", "(", ")"] 

morse_symbols_trasl = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",
                       ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                       "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
                       "..-", "...-", ".--", "-..-", "-.--", "--..", ".-.-.-", "--..--", "..--..", "-.-.--",
                       "-....-", "-..-.", ".--.-.", "-.--.", "-.--.-"]

# Наш словарь с кодами морзе для кодирования слов
morse_code = dict(zip(morse_symbols, morse_symbols_trasl))


# Начало программы
# Выводим сообщение пользователю

print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
input("Нажмите Enter и начнем ")


# Выводим список слов для тестирования пользователя
# в количессвте TOTAL_ANSWERS раз
for number in range(TOTAL_ANSWERS):
    #Получаем слово для тестирования пользователя
    user_test_word = get_random_word(word_list)
    template_morse_word = morse_encode(morse_code, user_test_word)
    # Для тестирования выводим правильное слово
    if DEBUG: print(f"Случайное слово № {number + 1} из списка >>> {user_test_word}")
    print(f"Слово {number + 1} >>> {template_morse_word}")
    user_variant = ""
    while user_variant == "":
        user_variant = input("Введите Ваш вариант: ").lower().strip()

    if user_variant == user_test_word:
        print(f"Верно, {user_variant} !")
        answers.append(True)
    else:
        print(f"Неверно, {user_test_word} !")
        answers.append(False)


print_statistics(answers)

############

