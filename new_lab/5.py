import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
students = pd.read_csv('students.csv')

# Гистограмма распределения баллов
plt.figure(figsize=(8, 6))  #размер граф
plt.hist(students['Score'], bins=10, color='skyblue', edgecolor='black')
plt.title('Распределение баллов')
plt.xlabel('Балл')
plt.ylabel('Количество студентов')
plt.grid(axis='y', alpha=0.5) #добавляем сетку
plt.show()


#ср балл по группам
avg_score_per_group = students.groupby('Group')['Score'].mean()
plt.figure(figsize=(8, 6))
avg_score_per_group.plot(kind='bar', color='lightcoral')
plt.title('Средний балл по группам')
plt.xlabel('Группа')
plt.ylabel('Средний балл')
plt.grid(axis='y', alpha=0.5)
plt.show()