from src.Product import Product


class LawnGrass(Product):
    """
    Класс для описания трава зеленая
    """

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """
        Для получения суммы всех товаров на складе нужно перемножить стоимость и количество всех товаров в наличии.
        :param other:
        :return summ:
        """
        if type(other) is LawnGrass:
            if not isinstance(other, LawnGrass):
                raise TypeError("Операция поддерживается только между объектами типа 'LawnGrass'")
            summ = self.price * self.quantity + other.price * other.quantity
            return summ
        raise TypeError
