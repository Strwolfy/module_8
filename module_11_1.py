import pandas as pd                 # 1-я библиотека
import numpy as np                  # 2-я библиотека
import matplotlib.pyplot as plt     # 3-я библиотека

# ==== демонстрация методов pandas ========= #

# Чтение данных из CSV файла
data = pd.read_csv("data.csv")

# Вывод первых 5 строк
print("Первые 5 строк данных:")
print(data.head())

# Группировка и расчет средней цены
avg_price = data.groupby("category")["price"].mean()
print("\nСредняя цена по категориям:")
print(avg_price)

# Фильтрация данных
filtered_data = data[data["price"] > 100]
print("\nТовары с ценой больше 100:")
print(filtered_data)

# ==== демонстрация методов numpy  ========= #

# Создание массива
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
squared = array ** 2
print("Квадраты элементов массива:")
print(squared)

# Создание матрицы и её транспонирование
matrix = np.array([[1, 2], [3, 4]])
transposed = matrix.T
print("\nТранспонированная матрица:")
print(transposed)

# Расчет среднего значения и стандартного отклонения
mean = np.mean(array)
std_dev = np.std(array)
print(f"\nСреднее значение: {mean}, Стандартное отклонение: {std_dev}")

# ==== демонстрация методов matplotlib ===== #

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Линейный график
plt.plot(x, y, label="Линейный график")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Пример графика")
plt.legend()
plt.show()

# Гистограмма
data = [5, 15, 25, 35, 45]
plt.hist(data, bins=5, color='blue', alpha=0.7)
plt.title("Гистограмма")
plt.show()

# Диаграмма рассеяния
plt.scatter(x, y, color='red')
plt.title("Диаграмма рассеяния")
plt.show()
