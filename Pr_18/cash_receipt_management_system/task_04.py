"""Система управления кассовыми чеками

04. Возврат по чеку

Доработайте Shift:

Добавьте метод add_return(shift, original_id, return_amount), где:
- shift: объект смены, в которой была покупка,
- original_id: ID исходного чека
- return_amount: сумму возврата

Метод проверяет,
- что в переданной смене существует чек с таким ID,
- в противном случае выбрасывается исключение:
    - ValueError("Original receipt not found.")

- что сумма возврата не превышает сумму этого чека
- в противном случае выбрасывается исключение:
    ValueError("Return amount exceeds original.")


Метод создаёт
- новый чек с отрицательной (!!!) суммой и

Метод добавляет
- этот созданные возвратный чек в текущую смену, как и обычные чеки
"""

from task_01 import Receipt

class Shift:
    pass





    def add_return(self, source_shift, original_id, return_amount):
        pass

