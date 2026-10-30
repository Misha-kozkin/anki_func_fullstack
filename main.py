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


def print_statistics(score: int, total_time: float) -> None:
    """Выводит итоговый счёт, общее и среднее время игры.

    Среднее время считается на один правильный ответ. Если правильных
    ответов нет, вместо среднего времени выводится прочерк.
    """
    game_time = format(total_time, '.2f')
    if score > 0:
        average = format(total_time / score, '.2f') + ' сек.'
    else:
        average = '—'
    print(f'Ваш итоговый счет: {score}')
    print(f'Время игры: {game_time} секунд (среднее время: {average})')


def ask_and_check(word: str, correct: str) -> Tuple[bool, bool, float]:
    """Спрашивает перевод слова и проверяет ответ.

    Возвращает кортеж из трёх значений: нужно ли выйти из игры,
    правильный ли ответ и сколько секунд занял ответ.
    Сравнение выполняется без учёта регистра и пробелов по краям.
    """
    print(f'Ваше слово: {word}')
    start_time = time.time()
    answer = input('Ваш перевод: ')
    end_time = time.time()
    if answer.strip().lower() == STOP_WORD.lower():
        return True, False, 0.0
    answer_time = end_time - start_time
    is_correct = answer.strip().lower() == correct.strip().lower()
    return False, is_correct, answer_time


def start_game(words):
    ...


def train_until_mistake(words):
    ...


def add_words(words: Dict[str, str]) -> None:
    """Добавляет в словарь новые пары «слово - перевод».

    Запрашивает у пользователя слово и перевод, пока не будет введено
    завершающее слово (без учёта регистра и пробелов по краям).
    Словарь изменяется на месте.
    """
    print(f'Чтобы закончить, введите {STOP_WORD}')
    while True:
        word = input('Введите слово: ').strip()
        if word.lower() == STOP_WORD.lower():
            break
        translation = input('Введите перевод: ').strip()
        if translation.lower() == STOP_WORD.lower():
            break
        if not word or not translation or ',' in word or ',' in translation:
            print('Ошибка: пустое значение или запятая. Пара не добавлена.')
            continue
        words[word] = translation


def show_all_words(words: Dict[str, str]) -> None:
    """Выводит все пары «слово - перевод» одной строкой через «; »."""
    pairs = []
    for word, translation in words.items():
        pairs.append(f'{word} - {translation}')
    print('; '.join(pairs))


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
