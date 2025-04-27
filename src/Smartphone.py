from src.Product import Product


class Smartphone(Product):
    """
    Класс для описания смартфонов
    """

    efficiency: float
    model: str
    memory: float
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """
        Для получения суммы всех товаров на складе нужно перемножить стоимость и количество всех товаров в наличии.
        :param other:
        :return summ:
        """
        if type(other) is Smartphone:
            if not isinstance(other, Smartphone):
                raise TypeError("Операция поддерживается только между объектами типа 'Smartphone'")
            summ = self.price * self.quantity + other.price * other.quantity
            return summ
        raise TypeError
