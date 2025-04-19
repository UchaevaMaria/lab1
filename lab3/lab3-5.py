class Student:  # создание класса
    def __init__(self, name, student_id):  # инициализация
        self.name = name
        self.student_id = student_id
        self.grades = []  # инициализация пустого списка для хранения оценок

    def add_grade(self, grade):  # метод для добавл оценок
        if 0 <= grade <= 10:  # проверяем по условию
            self.grades.append(grade)  # добавляем

    def get_average(self):
        if not self.grades:
            return 0.0  # если список оценок пуст
        return sum(self.grades) / len(self.grades)  # ср значение

    def display_info(self):  # метод для вывода инфо
        print("Студент", self.name)
        print('ID', self.student_id)
        print("Средний балл составляет:", self.get_average())

    def __str__(self):  #cтроковое представление
        return "Студент: " + self.name + ", ID: " + self.student_id + ", Средний балл: " + str(self.get_average())

    def __eq__(self, other):  #cравнение объектов 
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False  #если другие не является студенами значит ложь

    def __len__(self):  #количество оценок у студентов 
        return len(self.grades)
student1 = Student("Кирилл Ким", "1122145")  # создаем обьект
student1.add_grade(2)
student1.add_grade(7)
student1.add_grade(11)  # не добавится :/

print(student1)  #используем стрк
student2 = Student("Хелло Ворд", "112214567")
print(str(student1 == student2))  #используем eq