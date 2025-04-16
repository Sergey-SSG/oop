class Employee:  # Название класса
    # Одно из свойств класса - коэффициент повышения зарплаты
    raise_amount = 1.04  # Атрибут класса

    first: str  # Атрибуты (свойства) класса
    last: str
    pay: float

    def __init__(self, first, last, pay):  # Конструктор
        self.first = first  # Атрибуты (свойства) класса
        self.last = last
        self.pay = pay

    def apply_raise(self):  # Метод
        self.pay = self.pay * self.raise_amount
        return self.pay


# Создаем двух сотрудников
emp_1 = Employee('Ivan', 'Ivanov', 50000)
emp_2 = Employee('Petr', 'Petrov', 60000)


print(emp_1.apply_raise())
print(emp_2.apply_raise())