import pandas as pd
df = pd.read_csv('age_table1') # загрузка данных
mean_age = df['age'].mean()
above_average = df[df['age'] > mean_age]  #создание булевой маски,df - примен маски для филтрации
print(f"средний возраст сотрудников: {mean_age:1f} лет") #форматированный вывод среднего знач с округл до одного знака
print("сотрудники старше среднего возраста:")
print(above_average[['name', 'age']].to_string(index=False))  #вторая часть создана для красивого вывода без индексов панды 