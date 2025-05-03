import pytest

from src.Product import Product


def test_category_init(some_category, second_category):
    assert some_category.name == "Смартфоны"
    assert (
            some_category.description
            == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(some_category.add_product_in_list) == 2

    assert some_category.category_count == 2
    assert second_category.category_count == 2
    assert some_category.product_count == 190
    assert second_category.product_count == 190


def test_category_products_property(some_category):
    assert some_category.products == (
        " Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str(some_category):
    assert str(some_category) == "\nСмартфоны, количество продуктов: 22 шт.\n"


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == '55" QLED 4K'

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_middle_price(some_category, without_category):
    assert some_category.middle_price() == 120500.0
    assert without_category.middle_price() == 0


def test_custom_exception(capsys, some_category):
    assert len(some_category.products) == 92

    # product_add = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    # some_category.product = product_add
    # message = capsys.readouterr()
    # assert message.out.strip().split('\n')[-2] == "Отсутствует товар"
    # assert message.out.strip().split('\n')[-1] == "Успешно завершено"
