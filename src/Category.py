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
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)

    @property
    # def products(self):
    #     return "\n".join(
    #         [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    def products(self):
        product_str = " "
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def add_product_in_list(self):
        return self.__products
