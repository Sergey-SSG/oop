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
        self.price = price
        self.quantity = quantity
