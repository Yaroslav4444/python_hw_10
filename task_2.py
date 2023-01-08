"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


class NonNegative:
    """class for filtering attributes"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение этого аттрибута не может быть "
                             "отрицательным!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Cell:
    """creating Cell class"""
    quantity = NonNegative()

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f"({self.quantity})"

    def __add__(self, other):
        return f"Сумма клеток = {str(Cell(self.quantity + other.quantity))}"

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f"Разность клеток = {Cell(int(self.quantity - other.quantity))}"
        return "Разность отрицательна,операция не может быть выполнена"

    def __mul__(self, other):
        return f"Умножение клеток = {Cell(int(self.quantity * other.quantity))}"

    def __truediv__(self, other):
        return f"Деление клеток = {Cell((round(self.quantity // other.quantity)))}"

    def make_order(self, cells_count):
        """placing cells in rows"""
        my_row = ''
        for _ in range(int(self.quantity / cells_count)):
            my_row += f"{'*' * cells_count}\\n"
        my_row += f"{'*' * (self.quantity % cells_count)}"
        return my_row


print("Создаём объекты клеток")
cell1 = Cell(-100)
cell2 = Cell(75)

cell3 = Cell(30)
cell4 = Cell(45)

print()

print("Складываем объекты клеток")
print(cell1 + cell2)

print()

print("Вычитаем объекты клеток")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем объекты клеток")
print(cell2 * cell1)

print()

print("Делим объекты клеток")
print(cell1 / cell4)
