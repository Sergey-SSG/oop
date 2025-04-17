class Product:  # Название класса
    """ Класс для описания продуктов. """
    # Атрибуты (свойства) класса
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):  # Конструктор
        """ Метод для инициализации класса продуктов. Задаем значения атрибутам продуктов. """
        # Атрибуты (свойства) класса
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
