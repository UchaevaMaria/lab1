import pandas as pd

students = pd.read_csv('students.csv')

#группировка данных по столбцу 'Group'
grouped_data = students.groupby('Group').agg({
    'Score': 'mean',  # ср балл для каждой группы
    'Age': 'median'   
})
grouped_data = grouped_data.rename(columns={'Score': 'Average Score', 'Age': 'Median Age'}) #для удобства даю более понятные названия
#вывод данных
print("Сгруппированные данные:", grouped_data)
students['Passed'] = (students['Score'] >= 60).astype(int) #добавление столбца 'Passed'
print("Первые 5 строк с добавленным столбцом 'Passed'", students.head())
print("Сгруппированные данные с добавленным столбцом 'Passed':", students.groupby('Group')['Passed'].mean())