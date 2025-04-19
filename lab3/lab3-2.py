class Person: #создаем самый главный класс 
    def __init__(self, name, age): #инициал
        self.name = name
        self.age = age
class Student(Person): #класс студент зависит от род персон
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #вызываем из родительского класса
        self.student_id = student_id #даем id
class Teacher(Person): 
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = [] # создаем список, чтобы в него можно было добавить студентов
    def add_student(self, student): 
        if isinstance(student, Student):# если принадлежит 
            self.students.append(student) #добавляем 
            print("студент успешно добавлен :)")
        
    def remove_student(self, student): #удалить
        if student in self.students: # если студент находится в списке учащихся 
            self.students.remove(student) #удалить его
            print("студент удален :(")
    def list_students(self): #полная информация 
        if self.students:
            print("cписок студентов, которых преподает", self.name, self.subject,"(кол-во уч -", len(self.students),")")
            for student in self.students: #информация про студента, без оценок
                print(student.name, 'ID:', student.student_id)
    
    #проверка
if __name__ == "__main__":
    teacher = Teacher("Иван Иванов", 40, "Математика")
    student1 = Student("Анна Петрова", 20, "12345")
    student2 = Student("Борис Сидоров", 21, "67890")
    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.list_students()
    teacher.remove_student(student1)
    teacher.list_students()
