"""Система управления кассовыми чеками

03 Добавление чеков

Доработайте Shift, чтобы
- чеки создавались только (!) через смену
    (композиция или агрегация?)

А именно:
- добавьте в Shift метод add_receipt(), который:
    - Создаёт объект Receipt с уникальным ID
    - Сохраняет его внутри текущей смены
    - Если смена закрыта — выбрасывается ValueError:
        - ValueError("Cannot add receipts to a closed shift.")

Проверьте работу метода, создав несколько чеков внутри смены.
"""
from task_01 import Receipt

class Shift:
    pass



    def add_receipt(self, amount):
        pass



