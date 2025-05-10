from src.exceptions import ZeroQuantityProduct
from src.Product import Product


class Category:  # Название класса
    """
    Класс для описания категорий продуктов.
    """

    # Атрибуты (свойства) класса
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):  # Конструктор
        """
        Метод для инициализации класса категорий продуктов. Задаем значения атрибутам категорий продуктов.
        :param name:
        :param description:
        :param products:
        """
        # Атрибуты (свойства) класса
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __str__(self):
        return f"\n{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт.\n"

    @property
    def products(self):
        product_str = " "
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    # def products(self):
    #     return "\n".join(
    #         [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Отсутствует товар")
            except ZeroQuantityProduct as e:
                print(e)
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Успешно добавлено")
            finally:
                print("Успешно завершено")
        else:
            raise TypeError

    @property
    def add_product_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
