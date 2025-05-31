import pandas as pd
students = pd.read_csv('students.csv')
print('Вывод первых пяти:', students.head(), sep='\n')
print('Инфо:',students.info(), sep='\n')
print('Стата:', students.describe(), sep='\n')
avgs = students['Score'].mean() #вывод ср значение через метод mean()
print('Средний балл:', avgs, sep='\n') #выводим значение
amount_st = students.groupby('Group')['Group'].count() 
print('Количество студентов в группе:',amount_st, sep='\n') 