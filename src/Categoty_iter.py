# *
class CategoryIterator:
    """
    Создайте новый вспомогательный класс, с помощью которого можно перебирать товары одной категории, например в цикле for.
    Для этого новый класс должен принимать на вход объект класса категории и производить итерацию по товарам,
    которые хранятся в данной категории.
    То есть метод выполнения следующего шага итерации должен возвращать очередной товар категории.
    """

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.add_product_in_list):
            product = self.category.add_product_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
