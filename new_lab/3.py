import pandas as pd
students = pd.read_csv('students.csv')
#проверка наличия пропущенных значений
print("Проверка наличия пропущенных значений:\n", students.isnull().sum())

#заполнение пропущенных значений в столбце 'Score' средним значением, если нужно
score_mean = students['Score'].mean()
students['Score'].fillna(score_mean, inplace=True) #inplace чтобы изменить DataFrame
#проверка, остались ли пропуски в столбце 'Score'
print("\nПроверка после заполнения пропусков в 'Score':\n", students['Score'].isnull().sum())
students.dropna(subset=['Group'], inplace=True) #inplace чтобы изменить DataFrame
print("\nПроверка после удаления пропусков в 'Group':\n", students['Group'].isnull().sum())
print("\nПервые 5 строк DataFrame после обработки:\n", students.head())