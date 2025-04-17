from src.Product import Product


class Category:  # Название класса
    """ Класс для описания категорий продуктов. """

    # Атрибуты (свойства) класса
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):  # Конструктор
        """ Метод для инициализации класса категорий продуктов. Задаем значения атрибутам категорий продуктов. """
        # Атрибуты (свойства) класса
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)
