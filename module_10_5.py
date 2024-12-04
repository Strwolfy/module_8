import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat)

import time
from multiprocessing import Pool

def read_info(name):
    """Считывает информацию из файла построчно."""
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    # Список файлов
    filenames = [f'./data/file{number}.txt' for number in range(1, 5)]

    # Линейный вызов
    print("Линейный вызов:")
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    linear_time = time.monotonic() - start_time
    print(f"Линейный вызов: {linear_time:.2f} сек")

    # Многопроцессный вызов
    print("Многопроцессный вызов:")
    start_time = time.monotonic()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.monotonic() - start_time
    print(f"Многопроцессный вызов: {multiprocess_time:.2f} сек")
