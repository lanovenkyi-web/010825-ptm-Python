""" 01 Класс Student

Создайте класс Student, представляющий ученика.
При создании указываются имя и email.
Добавьте строковое представление студента (например, только имя).
Добавьте метод notify(message), который выводит сообщение: Email to <email>: <message>
Проверьте создание объекта и вызов метода.
"""

class Student:
    pass


student1 = Student("Иван", "ivan@example.com")

print(student1)  # Иван
student1.notify("Ваша домашняя работа проверена.")
# Email to ivan@example.com: Ваша домашняя работа проверена.
