class Student: #создание класса
    def __init__(self, name,student_id): #инициализация 
        self.name = name
        self.student_id = student_id
        self.grades = [] #инициализация пустого списка для хранения оценок
        
    def add_grade(self, grade): #метод для добавл оценок
        if 0<= grade<=10: #проверяем по условию
            self.grades.append(grade) #добавляем
    def get_average(self):
        if not self.grades:
            return 0.0 #если список оценок пуст
        return (sum(self.grades))/len(self.grades) #ср значение
    def display_info(self): #метод для вывода инфо
        print("Студент", self.name)
        print('ID', self.student_id)
        print("Средний балл составляет:", self.get_average())
if __name__ == "__main__":
    student = Student("Кирилл Ким", "1122145")
    
    student = Student("Кирилл Ким", "1122145") #создаем обьект
    student.add_grade(2)
    student.add_grade(7)
    student.add_grade(11)  # не добавится :/
    student.display_info() 
