import pandas as pd
students = pd.read_csv('students.csv')
high_scorers = students[students['Score'] > 80]#с баллом выше 80
#сортировка студентов по убыванию балла
high_scorers_sorted = high_scorers.sort_values(by='Score', ascending=False)
print("Студенты с баллом выше 80 (отсортировано по убыванию):\n", high_scorers_sorted)
oldest_student = students[students['Age'] == students['Age'].max()] #старший студент
print("\nСамый старший студент:\n", oldest_student)
youngest_student = students[students['Age'] == students['Age'].min()]#мл студент
print("\nСамый младший студент:\n", youngest_student)