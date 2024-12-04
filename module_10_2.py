import threading
import time

class Knight(threading.Thread):
    enemies = 100  # Общее количество врагов для всех рыцарей
    enemies_lock = threading.Lock()  # Блокировка для синхронизации доступа

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0

        while True:
            with Knight.enemies_lock:
                if Knight.enemies <= 0:
                    break
                defeated = min(self.power, Knight.enemies)
                Knight.enemies -= defeated

            days += 1
            time.sleep(1)
            print(f"{self.name} сражается {days} день(дня)..., осталось {Knight.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
