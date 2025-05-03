from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin


class Product(BaseProduct, PrintMixin):  # Название класса
    """
    Класс для описания продуктов.
    """

    # Атрибуты (свойства) класса
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):  # Конструктор
        """
        Метод для инициализации класса продуктов. Задаем значения атрибутам продуктов.
        :param name:
        :param description:
        :param price:
        :param quantity:
        """
        # Атрибуты (свойства) класса
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Для получения суммы всех товаров на складе нужно перемножить стоимость и количество всех товаров в наличии.
        :param other:
        :return summ:
        """
        if type(other) is Product:
            if not isinstance(other, Product):
                raise TypeError("Операция поддерживается только между объектами типа 'Product'")
            summ = self.__price * self.quantity + other.__price * other.quantity
            return summ
        raise TypeError

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
