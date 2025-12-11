""" 02 Класс Course

Создайте класс Course, представляющий учебный курс.
При создании указывается название курса.
У каждого объекта Course должен быть
- атрибут students, в котором хранится список зарегистрированных студентов.

Добавьте метод add_student(student), который принимает объект Student и добавляет его в курс.
Добавьте метод show_students(), который выводит список имён студентов.
Добавьте метод notify_all(message), который уведомляет всех студентов курса.

Проверьте работу методов, создав курс, добавив студентов и отправив уведомление.

Пример вывода:
Students enrolled in Python OOP:
- Alice
- Bob

Email to alice@example.com: Welcome to the course!
Email to bob@example.com: Welcome to the course!
"""

class Student:
    pass


class Course:
    pass


course = Course("Python OOP")

alice = Student("Alice", "alice@example.com")
bob = Student("Bob", "bob@example.com")

course.add_student(alice)
course.add_student(bob)
course.show_students()
course.notify_all("Welcome to the course!")

# Students enrolled in Python OOP:
# - Alice
# - Bob
# Email to alice@example.com: Welcome to the course!
# Email to bob@example.com: Welcome to the course!