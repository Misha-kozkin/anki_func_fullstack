import random
import sys
import time
from typing import Dict, Tuple


STOP_WORD = 'СТОП'


def load_words(filename: str = 'words.txt') -> Dict[str, str]:
    """Загружает словарь слов из файла words.txt.

    Каждая строка файла должна иметь вид «слово,перевод».
    Строки без запятой или с лишними запятыми пропускаются.
    Если файл не найден, выводит сообщение и завершает программу
    с кодом 1.
    """
    words = {}
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                ports = line.strip().split(',')
                if len(ports) == 2:
                    word, translation = ports
                    words[word] = translation
    except FileNotFoundError:
        print(f'Файл {filename} не найден')
        sys.exit(1)
    return words


def print_statistics(score, total_time):
    ...


def ask_and_check(word, correct):
    ...


def start_game(words):
    ...


def train_until_mistake(words):
    ...


def add_words(words):
    ...


def show_all_words(words):
    ...


def save_words(words: Dict[str, str], filename: str = 'words.txt') -> None:
    """Сохраняет словарь слов в файл.

    Каждая пара записывается в отдельную строку в формате «слово,перевод».
    Если файл уже существует, его содержимое перезаписывается.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for word, translation in words.items():
            file.write(word + ',' + translation + '\n')
    print(f'Было сохранено {len(words)} словo в фаил {filename}')
    

def main():
    while True:
        menu = '''Меню:
        1. Начать игру
        2. Добавить слова
        3. Тренировка до первой ошибки
        4. Вывод всех слов
        5. Выход
        '''
        print(menu)
        menu_choice = input('Пункт меню: ')


if __name__ == '__main__':
    main()
