"""Система управления кассовыми чеками

05. Классы SaleReceipt и ReturnReceipt

Доработайте систему чеков:
- создайте 2 дочерних класса
    - SaleReceipt(Receipt) и
    - ReturnReceipt(Receipt)


При создании SaleReceipt
- проверяйте, что сумма положительная

При создании ReturnReceipt
- проверяйте, что сумма отрицательная

В обоих случаях, если сумма нарушает правило, выбрасывается ValueError:
- ValueError("SaleReceipt amount must be positive.")
- ValueError("ReturnReceipt amount must be negative.")

Добавьте метод __str__(), возвращающий строку в формате:
<ReceiptClass> <ID>: +<amount>
<ReceiptClass> <ID>: -<amount>
"""

class Receipt:
    pass



class SaleReceipt(Receipt):
    pass


class ReturnReceipt(Receipt):
    pass


